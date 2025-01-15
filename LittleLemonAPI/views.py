from django.shortcuts import render 
from rest_framework.response import Response 
from rest_framework import serializers
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.generics import ListCreateAPIView , RetrieveDestroyAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated



class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
    

class SingleMenuItemView(RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    


@api_view()
@permission_classes([IsAuthenticated])# @authentication_classes([TokenAuthentication])
def msg(request):
     return Response({"message":"This view is protected"})