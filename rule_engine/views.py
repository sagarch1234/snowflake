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
from rule_engine.models import OneQueryRules, Audits, AuditsResults, IgnoreRules, AuditStatus, DoNotNotifyUsers

from system_users.permissions import WhitelistOrganisationAdmin, WhitelistOrganisationMember, WhitelistSuperAdmin
from snowflake_instances.permissions import IsInstanceAccessible

from rule_engine.rules_utility import get_instance, connect_to_customer_sf_instance, prepare_rule_set


class ListOneQueryRuleView(ListAPIView):    
    '''
    This method list the Rules along with its articles - which were created by the super admin.
    '''
    permission_classes = [(WhitelistOrganisationAdmin | WhitelistOrganisationMember | WhitelistSuperAdmin) & IsAuthenticated]

    def get_queryset(self):
        '''
        '''
        user_group = self.request.user.groups.get().name

        if user_group == 'Super Admin':

            queryset = OneQueryRules.objects.all() 
        
        else:

            queryset = OneQueryRules.objects.filter(is_enabled=True)

        return queryset 

    
    serializer_class = OneQueryRuleSerializer
    pagination_class = PageNumberPagination
    filter_backends = [OrderingFilter, SearchFilter, DjangoFilterBackend]
    filterset_fields = ['is_enabled']
    search_fields = ['rule_name']
    ordering=['-id']


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
    '''
    permission_classes = [(WhitelistOrganisationAdmin | WhitelistOrganisationMember) & IsAuthenticated]

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
            "message" : "User added to do not notifity list for this instance.",
            "status" : status.HTTP_200_OK
        })


class RemoveDoNotNotifyUsersView(APIView):
    
    def post(self, request, format=None):
        ''' 
        '''
        try:

            obj = DoNotNotifyUsers.objects.get(instance=request.data['instance'], user=request.data['user'])

        except Exception as identifier:
            
            return Response({
                "error" : str(identifier),
                "status" : status.HTTP_404_NOT_FOUND
            })

        obj.delete()

        return Response({
            "message":"User will be notified.",
            "status" : status.HTTP_200_OK
        })


class UpdateRuleView(APIView):
    '''
    '''
    
    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]

    def put(self, request, format=None):
        '''
        '''

        instance = get_object_or_404(OneQueryRules, pk=request.query_params['rule_id'])

        serialized_data = OneQueryRuleSerializer(instance, data=request.data, context={'articles': request.data['one_query_rule_related_articles']}, partial=True)
        
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









class ListAuditsView(ListAPIView):
    '''
    '''
    permission_classes = [IsAuthenticated & IsInstanceAccessible]

    serializer_class = AuditsSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['status']
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






class RunAuditView(APIView):
    '''
    '''
    
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        # get instance_id in query_params.
        # call get_instance method if instance not found then return appropriate message.

        customer_instance = get_instance(request.query_params['instance_id'])

        if customer_instance == status.HTTP_404_NOT_FOUND:

            return Response({
                "error" : "Unable to find this instance.",
                "status" : customer_instance
            })

        #get the list of all the Audit status.
        audit_status_list = AuditStatus.objects.all()

        # generate the 'audit_id' with status connecting.
        audit_instance = Audits.objects.create(instance = customer_instance, status=audit_status_list[0], user=request.user)

        connection = connect_to_customer_sf_instance(user=customer_instance.instance_user , password=customer_instance.instance_password , account=customer_instance.instance_account , audit_id=audit_instance.id)
        rule_list = prepare_rule_set(customer_instance.id)
        
        return Response({
            "message" : "This might take a while. We will notify you via mail.",
            "status" : status.HTTP_200_OK
        })
        


