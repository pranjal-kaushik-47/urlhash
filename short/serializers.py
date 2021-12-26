from rest_framework import serializers
from .models import Urls

class ShortUrlSerializers(serializers.ModelSerializer):

    class Meta:
        model = Urls
        fields = '__all__'
        extra_kwargs = {
            'record_id': {'required': False},
            'hash': {'required': False}
            }