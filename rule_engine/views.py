from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend

from rule_engine.serializers import OneQueryRuleSerializer
from rule_engine.models import OneQueryRules

class CreateOneQueryRuleView(APIView):
    '''
    '''
    def post(self, request, fromat=None):
        '''
        '''

        serialized_data = OneQueryRuleSerializer(data=request.data)

        if serialized_data.is_valid():

            created_rule = serialized_data.save()

            return Response({
                "message":"A new one query rule is registered and enabled for the audits.",
                "status":status.HTTP_200_OK
            })
        
        else:

            return Response(serialized_data.errors)


class ListOneQueryRuleView(ListAPIView):
    '''
    '''
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