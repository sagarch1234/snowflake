from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from advertisement.serializers import AdvertisementSerializer
from advertisement.models import Advertisement

from django_filters.rest_framework import DjangoFilterBackend

from system_users.permissions import WhitelistSuperAdmin, WhitelistOrganisationMember, WhitelistOrganisationAdmin


class ShowAdvertisementsView(ListAPIView):
    '''
    '''

    permission_classes = [IsAuthenticated & (WhitelistSuperAdmin | WhitelistOrganisationMember | WhitelistOrganisationAdmin)]
    
    # queryset = Advertisement.objects.filter(is_applied=True)
    serializer_class = AdvertisementSerializer
    filter_backends = [OrderingFilter]
    ordering=['-id']

    def get_queryset(self):

        return Advertisement.objects.filter(is_applied=True)



class CreateAdvertisementView(APIView):

    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]
    
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):

        serialized_data = AdvertisementSerializer(data=request.data)

        if serialized_data.is_valid():

            advertisement_instance = serialized_data.save()

            return Response({
                "message" : "Advertisement banners added.",
                "status" : status.HTTP_200_OK
            })

        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAdvertisementView(ListAPIView):

    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['side', 'is_applied']
    ordering=['-id']
    pagination_class = PageNumberPagination


class EnableDisableAdvertisementView(APIView):

    permission_classes = [IsAuthenticated & WhitelistSuperAdmin]
    
    def put(self, request, format=None):

        advertisement_instance = get_object_or_404(Advertisement, pk=request.query_params['id'])

        if advertisement_instance.is_applied == True:

            return Response({
                "error" : "Advertisement already published.",
                "status" : status.HTTP_400_BAD_REQUEST
            })
        elif advertisement_instance.is_applied == False:

            all_advertisement = Advertisement.objects.filter(side=advertisement_instance.side).update(is_applied=False)

            advertisement_instance.is_applied = True
            
            advertisement_instance.save()
            
            return Response({
                "message" : "Selected advertisement has been puslished.",
                "status" : status.HTTP_200_OK
            })
