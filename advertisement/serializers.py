from rest_framework import serializers
from advertisement.models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    '''
    This serializer is to create retrive and update advertisement banner.
    '''
    class Meta:
        model = Advertisement
        fields = '__all__'
        