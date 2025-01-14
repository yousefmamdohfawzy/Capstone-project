from django.shortcuts import render
from rest_framework.generics import  ListCreateAPIView ,RetrieveUpdateDestroyAPIView
from .serializers import Bookingserializer , Menuserializer
from .models import Menu , Booking
from rest_framework import viewsets
# from rest_framework.permissions import IsAuthenticated
# from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



    #     Handles GET and POST requests for menu items.
class MenuItemsView (ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer

    #  Handles GET, PUT, and DELETE requests for a single menu item
class SingleMenuItemView (RetrieveUpdateDestroyAPIView ):
    queryset = Menu.objects.all()
    serializer_class = Menuserializer


#    Handles CRUD operations for Booking model.
class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = Bookingserializer 





#Api viewset
# class UserViewSet (viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated]
    
    
    
