from rest_framework import serializers
from .models import Advertising

class AdvertisingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertising
        fields = ('company_name', 'description')

class AdvertisingFullSerializer(AdvertisingSerializer):

    class Meta(AdvertisingSerializer.Meta):
        fields = AdvertisingSerializer.Meta.fields + ('image',)