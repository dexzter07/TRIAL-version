from django.shortcuts import render
from app1.models import Customer
from app1.serializers import Homes
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(('POST',))
def home(request):
    if request.method=="POST":
        object = Homes(data=request.data)
        if object.is_valid():
            object.save()
            context={"message":"SUCCESS!"}
        else:
            context={"message":"UNSUCCESS!"}
        return Response(context)
