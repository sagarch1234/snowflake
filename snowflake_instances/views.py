import jwt

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Group

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from snowflake.instance_connector.connection import SnowflakeConnector, CloseSnowflakeConnection, DisposeEngine

from snowflake_instances.serializers import InstancesSerializer, AccountTypeSerializer
from snowflake_instances.models import Instances, InstanceAccountType
from snowflake_instances.permissions import IsInstanceAccessible
from snowflake_instances.tasks import parameters_and_instance_data
# from snowflake_instances.tasks import ParametersAndInstanceData

from snowflake_optimizer.settings import SECRET_KEY

from system_users.permissions import WhitelistOrganisationAdmin, WhitelistOrganisationMember, WhitelistSuperAdmin
from system_users.constants import SUPER_ADMIN

from snowflake_optimizer.settings import SECRET_KEY

from snowflake_optimizer.celery import app



class ListAccountTypeView(ListAPIView):
    '''
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationMember | WhitelistOrganisationAdmin)]

    serializer_class = AccountTypeSerializer

    filter_backends = [OrderingFilter]
    
    ordering = ['-id']
        
    def get_queryset(self):
    
        return InstanceAccountType.objects.all()


class AddInstanceView(APIView):
    '''
    This view is for Organisation Admins to add instances to the systems.
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember)]

    def post(self, request, format=None):
        
        serialized_data = InstancesSerializer(data=request.data)

        if serialized_data.is_valid():
            
            #check and connect to instance
            instance = SnowflakeConnector(request.data['instance_user'], request.data['instance_password'], request.data['instance_account'], 'ACCOUNTADMIN')
            connection = instance.connect_snowflake_instance()
            
            #if snowflake instance connected
            if connection['status'] == status.HTTP_200_OK:
                
                #encrypt instance password.
                encoded_password = jwt.encode({"password":request.data['instance_password']}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                
                serialized_data.validated_data['instance_password'] = encoded_password

                #foreign key instances
                serialized_data.validated_data['created_by'] = request.user
                serialized_data.validated_data['company'] = request.user.company

                #add instance details to the database.
                instance_object = serialized_data.save()

                #close instance connection
                close_instance = CloseSnowflakeConnection(connection['connection_object'])
                close_instance.close_connected_instance()             

                #dispose engine
                dispose_engine = DisposeEngine(connection['engine'])
                dispose_engine.close_engine()

                #add a task to the celery.
                #This task will fetch initial data from customer's instances.
                parameters_and_instance_data.delay(request.data['instance_user'], request.data['instance_password'], request.data['instance_account'], instance_object.id)

                return Response({
                    "message":"Connection to the Snowflake instance was successful.",
                    "status":status.HTTP_200_OK
                })

            #return error if failed to connect to instance using provided credentials.
            elif connection['status'] == status.HTTP_400_BAD_REQUEST:

                return Response(connection)
                                    
        else:

            #return error if serialization of data has failed.
            return Response(serialized_data.errors)


class ListInstancesView(ListAPIView):
    '''
    This view will list all the instances of a company.
    Authentication is required to access this view.
    If authenticated user is of type ```SUPER ADMIN``` then provide ```comapny_id``` as a ```query_parameter```.
    ```comapny_id``` as a ```query_parameter``` is not required if authenticated user is of type other then  ```SUPER ADMIN```.
     
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationMember | WhitelistOrganisationAdmin | WhitelistSuperAdmin)]

    serializer_class = InstancesSerializer

    filter_backends = [OrderingFilter, SearchFilter]
    
    ordering = ['-id']
    
    search_fields = ['instance_name']
    
    pagination_class = PageNumberPagination

    def get_queryset(self):

        current_user_group = list(self.request.user.groups.values('name'))

        if str(Group.objects.get(name=SUPER_ADMIN)) == current_user_group[0]['name']:

            return Instances.objects.filter(company=self.request.query_params['company_id'])
    
        return Instances.objects.filter(company=self.request.user.company)


class UpdateInstanceview(APIView):
    '''
    To update the instace credentials.
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember) & IsInstanceAccessible]

    def put(self, request, format=None):

        instance_object = get_object_or_404(Instances, pk=request.query_params['instance_id'])
        
        serialized_data = InstancesSerializer(instance_object, data=request.data, partial=False)

        if serialized_data.is_valid():
            
            #try connecting to the snowflake instance using provided credentials.
            instance = SnowflakeConnector(request.data['instance_user'], request.data['instance_password'], request.data['instance_account'], 'ACCOUNTADMIN')
            connection = instance.connect_snowflake_instance()
                        
            if connection['status'] == status.HTTP_200_OK:

                #close instance connection
                close_instance = CloseSnowflakeConnection(connection['connection_object'])
                close_instance.close_connected_instance()

                #dispose engine
                dispose_engine = DisposeEngine(connection['engine'])
                dispose_engine.close_engine()

                #encrypt instance password.
                serialized_data.validated_data['instance_password'] = jwt.encode({"password":serialized_data.validated_data['instance_password']}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                
                updated_instance = serialized_data.save()
                
                return Response({
                    "message":"Connection Successful. Instance details updated.",
                    "status" : status.HTTP_200_OK
                })

            elif connection['status'] == status.HTTP_400_BAD_REQUEST:

                return Response(connection)
        
        else:
        
            return Response(serialized_data.errors)


class ReconnectAllInstancesView(APIView):
    '''
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember)]

    def post(self, request, format=None):

        connection_refused = []
        connected_instances = []
        
        instance_list = Instances.objects.filter(company=request.user.company)

        for instance in instance_list:

            decoded_password = jwt.decode(instance.instance_password, SECRET_KEY, algorithms=['HS256'])

            connected_instance = SnowflakeConnector(instance.instance_user, decoded_password['password'], instance.instance_account, 'ACCOUNTADMIN')
            
            connection = connected_instance.connect_snowflake_instance()
            
            if connection['status'] == status.HTTP_200_OK:
            
                serialized_instance = InstancesSerializer(instance)
                
                connected_instances.append(serialized_instance.data)

                #close instance connection
                close_instance = CloseSnowflakeConnection(connection['connection_object'])
                close_instance.close_connected_instance()

                #dispose engine
                dispose_engine = DisposeEngine(connection['engine'])
                dispose_engine.close_engine()


            elif connection['status'] == status.HTTP_400_BAD_REQUEST:

                serialized_instance = InstancesSerializer(instance)

                instance = serialized_instance.data

                instance['issue'] = connection

                connection_refused.append(instance)

        return Response({
            "connected_instances" : connected_instances,
            "could_not_connect" : connection_refused
        })
        

class ReconnectInstanceView(APIView):
    '''
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember) & IsInstanceAccessible]

    def post(self, request, format=None):
        
        instance_object = get_object_or_404(Instances, pk=request.query_params['instance_id'])

        decoded_password = jwt.decode(instance_object.instance_password, SECRET_KEY, algorithms=['HS256'])

        instance = SnowflakeConnector(instance_object.instance_user, decoded_password['password'], instance_object.instance_account, 'ACCOUNTADMIN')
        connection = instance.connect_snowflake_instance()

        if connection['status'] == status.HTTP_200_OK:

            #close instance connection
            close_instance = CloseSnowflakeConnection(connection['connection_object'])
            close_instance.close_connected_instance()

            #dispose engine
            dispose_engine = DisposeEngine(connection['engine'])
            dispose_engine.close_engine()
            
            return Response({
                "message" :"Connection successful.",
                "status" : status.HTTP_200_OK
            })
            
        elif connection['status'] == status.HTTP_400_BAD_REQUEST:

            return Response(connection)


class RemoveInstanceView(APIView):
    '''
    '''
    
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember) & IsInstanceAccessible]

    def delete(self, request, format=None):

        instance_object = get_object_or_404(Instances, pk=request.query_params['instance_id'])
        
        instance_object.delete()
        
        return Response({
            "message":"Snowflake instance deleted.",
            "status":status.HTTP_200_OK
        })