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

from snowflake_connector.connection import connect_snowflake_instance
from snowflake_connector.serializers import InstancesSerializer
from snowflake_connector.models import Instances
from snowflake_connector.permissions import IsInstanceAccessible

from snowflake_optimizer.settings import SECRET_KEY

from system_users.permissions import WhitelistOrganisationAdmin, WhitelistOrganisationMember, WhitelistSuperAdmin
from system_users.constants import SUPER_ADMIN

import jwt

from snowflake_optimizer.settings import SECRET_KEY


class AddInstanceView(APIView):
    '''
    This view is for Organisation Admins to add instances to the systems.
    '''
    permission_classes = [IsAuthenticated & (WhitelistOrganisationAdmin | WhitelistOrganisationMember)]

    def post(self, request, format=None):
        
        serialized_data = InstancesSerializer(data=request.data)

        if serialized_data.is_valid():
            
            #check and connect to instance

            connection = connect_snowflake_instance(request.data['instance_user'], request.data['instance_password'], request.data['instance_account']) 

            #if snowflake instance connected

            if connection['status'] == status.HTTP_200_OK:
                
                #encrypt instance password.
                encoded_password = jwt.encode({"password":request.data['instance_password']}, SECRET_KEY, algorithm='HS256').decode('utf-8')
                
                serialized_data.validated_data['instance_password'] = encoded_password
                serialized_data.validated_data['created_by'] = request.user
                serialized_data.validated_data['company'] = request.user.company

                #add instance details to the database.

                instance_object = serialized_data.save()

                return Response({
                    "message":"Connection to the Snowflake database was successful.",
                    "status":status.HTTP_200_OK
                })

            elif connection['status'] == status.HTTP_400_BAD_REQUEST:

                return Response(connection)
                                    
        else:

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
            
            connection = connect_snowflake_instance(serialized_data.validated_data['instance_user'], serialized_data.validated_data['instance_password'], serialized_data.validated_data['instance_account'])
            
            if connection['status'] == status.HTTP_200_OK:

                serialized_data.validated_data['company'] = request.user.company
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
        
        instnaces_list = Instances.objects.filter(company=request.user.company)

        for instnace in instnaces_list:

            decoded_password = jwt.decode(instnace.instance_password, SECRET_KEY, algorithms=['HS256'])

            connection = connect_snowflake_instance(instnace.instance_user, decoded_password['password'], instnace.instance_account)

            if connection['status'] == status.HTTP_200_OK:
            
                serialized_instance = InstancesSerializer(instnace)
                
                connected_instances.append(serialized_instance.data)


            elif connection['status'] == status.HTTP_400_BAD_REQUEST:

                serialized_instance = InstancesSerializer(instnace)

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

        print(instance_object.instance_user, decoded_password, instance_object.instance_account)

        connection = connect_snowflake_instance(instance_object.instance_user, decoded_password['password'], instance_object.instance_account)

        if connection['status'] == status.HTTP_200_OK:
            
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
            "message":"Snowflake database instance deleted.",
            "status":status.HTTP_200_OK
        })