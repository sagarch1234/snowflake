from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from rule_engine.serializers import OneQueryRuleSerializer, AuditsSerializer, AuditsResultsSerializer, IgnoreRulesSerializer, DoNotNotifyUsersSerializer
from rule_engine.models import OneQueryRules, Audits, AuditsResults, IgnoreRules

from system_users.permissions import WhitelistSuperAdmin
from snowflake_instances.permissions import IsInstanceAccessible


class ListAuditsView(ListAPIView):
    '''
    Need to test.
    '''
    permission_classes = [IsInstanceAccessible & IsAuthenticated]

    serializer_class = AuditsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['status']
    ordering = ['-id']

    def get_queryset(self):

        queryset = Audits.objects.filter(instance=self.request.query_params['instance_id'])

        return queryset


class ListAuditResultsView(ListAPIView):
    '''
    Need to test.
    '''
    permission_classes = [IsAuthenticated]

    serializer_class = AuditsResultsSerializer
    ordering = ['-id']

    def get_queryset(self):

        queryset = AuditsResults.objects.filter(audit=self.request.query_params['audit_id'])

        return queryset
        

class CreateOneQueryRuleView(APIView):
    '''
    '''
    
    permission_classes = [WhitelistSuperAdmin & IsAuthenticated]

    def post(self, request, fromat=None):
        '''
        '''

        serialized_data = OneQueryRuleSerializer(data=request.data)

        if serialized_data.is_valid():

            try:
                
                created_rule = serialized_data.save()

            except Exception as identifier:

                return Response({
                    "error" : str(identifier),
                    "status" : status.HTTP_400_BAD_REQUEST
                    })
            

            return Response({
                "message":"A new one query rule is registered and enabled for the audits.",
                "status":status.HTTP_200_OK
            })
        
        else:

            return Response(serialized_data.errors)


class ListOneQueryRuleView(ListAPIView):
    '''
    '''
    
    permission_classes = [WhitelistSuperAdmin & IsAuthenticated]

    serializer_class = OneQueryRuleSerializer
    pagination_class = PageNumberPagination
    filter_backends = [OrderingFilter, SearchFilter]
    filterset_fields = ['is_enabled']
    search_fields = ['rule_name']
    ordering=['-id']
    queryset = OneQueryRules.objects.all()


class EnableDisableOneQueryRuleView(APIView):
    '''
    In query params provide 'one_query_rule_id'.
    In request payoad provide 'is_enabled' as key and 'true' or 'false' as value.
    '''

    permission_classes = [WhitelistSuperAdmin & IsAuthenticated]
    
    def put(self, request, format=None):
        '''
        '''

        if 'is_enabled' in request.data:

            rule_object = get_object_or_404(OneQueryRules, pk=request.query_params['one_query_rule_id'])

            if rule_object.is_enabled == request.data['is_enabled']:

                return Response({
                    "message" : "'is_enabled' flag for the rule is already " + str(rule_object.is_enabled),
                    "status":status.HTTP_200_OK
                })
            
            else:

                rule_object.is_enabled = request.data['is_enabled']

                rule_object.save()

                return Response({
                    "message":"'is_enabled' flag for the rule has been updated to " + str(rule_object.is_enabled),
                    "status" : status.HTTP_200_OK
                })

        else:
            return Response({
                "message":"Invalid Payload.",
                "status" : status.HTTP_404_NOT_FOUND
            })


class AddRuleToIgnoreListView(APIView):
    '''
    '''
    
    permission_classes = [IsAuthenticated & IsInstanceAccessible]

    def post(self, request, format=None):
        '''
        '''
        
        request.data['instance'] = request.query_params['instance_id']

        serialized_data = IgnoreRulesSerializer(data=request.data)

        if serialized_data.is_valid():

            try:
                
                serialized_data.validated_data['user'] = request.user

                ignored_rule_instance = serialized_data.save()

            except Exception as identifier:

                return Response({
                    "error" : str(identifier),
                    "status" : status.HTTP_400_BAD_REQUEST
                    })
            
            return Response({
                "message" : "Rule added to ignore list.",
                "status" : status.HTTP_200_OK
            })

        else:
            
            return Response(serialized_data.errors)


class RemoveRuleFromIgnoreListView(APIView):
    '''
    '''

    permission_classes = [IsAuthenticated & IsInstanceAccessible]

    def delete(self, request, format=None):
        '''
        '''
        try:

            ignored_rule_object = IgnoreRules.objects.get(one_query_rule=request.query_params['rule_id'], instance=request.query_params['instance_id'])

        except Exception as identifier:

            return Response({
                    "error" : str(identifier),
                    "status" : status.HTTP_400_BAD_REQUEST
                    })

        ignored_rule_object.delete()
        
        return Response({
            "message" : "Rule removed from ignore list of this instance."
        })


class DoNotNotifyUsersView(APIView):
    '''
    Need to test.
    By default this will notify to each user of that organistaion.

    '''
    def post(self, request, format=None):
        '''
        '''
        
        serialized_data = DoNotNotifyUsersSerializer(data=request.data)

        if serialized_data.is_valid():
            
            try:
                
                created_object = serialized_data.save()

            except Exception as identifier:
                
                return Response({
                    "error" : str(identifier),
                    "status" : status.HTTP_400_BAD_REQUEST
                    })
            
        else:
            
            return Response(serialized_data.errors)

        return Response({
            "message" : "User added to do not notifity list for this Audit.",
            "status" : status.HTTP_200_OK
        })


class RunAuditView(APIView):
    '''
    '''
    def post(self, request, format=None):

        # get instance_id in query_params.
        # call get_instance method if instance not found then return appropriate message.
        # generate the 'audit_id' with status connecting.
        # use the sf_instance to get the sf connection credentials and try to connect to sf_instance. If failed to connect then update status to connection error. store the connection error in db. 
        # get the final list of rules. 
        # apply each rule and prepare the list of all the passed and failed rules (with recommendation)
        
        pass


class UpdateRuleView(APIView):
    '''
    '''
    def put(self, request, format=None):
        '''
        '''
        instance = get_object_or_404(OneQueryRules, pk=request.query_params['rule_id'])

        serialized_data = OneQueryRuleSerializer(instance, data=request.data, partial=True)
        
        if serialized_data.is_valid():

            try:
                
                updated_instance = serialized_data.save()

            except Exception as identifier:
                
                return Response({
                    "error" : str(identifier),
                    "status" : status.HTTP_400_BAD_REQUEST
                    })

        else:

            return Response(serialized_data.errors)

        return Response({
            "message" : "Rule updated.",
            "status" : status.HTTP_200_OK
        })