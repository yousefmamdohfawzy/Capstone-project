from django.test import TestCase, Client 
from rest_framework.test import APIClient
from django.urls import reverse
# from Restaurant.views import MenuItemsView
from Restaurant.models import Menu
from Restaurant.serializers import Menuserializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class  MenuViewTest (TestCase):
    
            # Add test instances of the Menu model
    def setUp(self):
          # Create a test user and generate a token
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)
        
        # Set up the test client with authentication
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

            # Create menu items
        self.menuitem1 = Menu.objects.create(title="Pizza", price=10.99, inventory=50)
        self.menu_item2 = Menu.objects.create(title="Burger", price=5.99, inventory=30)
        self.menu_item3 = Menu.objects.create(title="Pasta", price=8.99, inventory=20)
        
          # Define the URL for the MenuItemsView
        self.menu_url = reverse('menu')
        
    def test_getall(self):
        # Perform a GET request to retrieve all Menu objects
        response = self.client.get(self.menu_url)
        
          # Serialize the data manually
        menu_items = Menu.objects.all()
        serialized_data = Menuserializer (menu_items,many=True).data
        
                # Assert the response status code
        self.assertEqual(response.status_code,200)
        
         # Assert the serialized data matches the response data
        self.assertEqual (response.json(),serialized_data)