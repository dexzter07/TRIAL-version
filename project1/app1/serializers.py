from rest_framework import serializers
from app1.models import Customer

class Homes(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
