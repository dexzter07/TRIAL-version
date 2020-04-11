from rest_framework import serializers
from app1.models import Customer


class Homes(serializers.ModelSerializer):
    name = serializers.RelatedField(source='user', read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
