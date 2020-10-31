import jwt

from django.shortcuts import render, get_object_or_404

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

from snowflake_optimizer.settings import SECRET_KEY

from system_users.permissions import WhitelistOrganisationAdmin


class AddInstanceView(APIView):
    '''
    This view is for Organisation Admins to add instances to the systems.
    '''
    permission_classes = [IsAuthenticated & WhitelistOrganisationAdmin]

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
    '''
    permission_classes = [IsAuthenticated]

    serializer_class = InstancesSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    ordering = ['-id']
    search_fields = ['instance_name']
    pagination_class = PageNumberPagination

    def get_queryset(self):
        return Instances.objects.filter(company=self.request.user.company)


class UpdateInstanceview(APIView):
    '''
    To update the instace credentials.
    '''

    def put(self, request, format=None):

        instance_object = get_object_or_404(Instances, pk=request.query_params['instance_id'])
        
        serialized_data = InstancesSerializer(instance_object, data=request.data, partial=False)

        if serialized_data.is_valid():
            
            connection = connect_snowflake_instance(serialized_data.validated_data['instance_user'], serialized_data.validated_data['instance_password'], serialized_data.validated_data['instance_account'])
            
            if connection['status'] == status.HTTP_200_OK:
                
                updated_instance = serialized_data.save()
                
                return Response({
                    "message":"Connection Successful. Instance details updated.",
                    "status" : status.HTTP_200_OK
                })

            elif connection['status'] == status.HTTP_400_BAD_REQUEST:
                return Response(connection)
        else:
            return Response(serialized_data.errors)
