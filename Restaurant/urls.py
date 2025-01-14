#define URL route for index() view
from django.urls import path , include
from . import views
# from rest_framework import routers    #Apiviewset


# api viewset
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

urlpatterns = [
    
    path('index', views.index, name='index'),
      
        #generic view 
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
    # path('', include(router.urls)), #Api viewset
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),#Api viewset
    
]
