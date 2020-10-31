from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from snowflake_connector.connection import connect_snowflake_instance
from snowflake_connector.serializers import InstancesSerializer

import jwt

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
