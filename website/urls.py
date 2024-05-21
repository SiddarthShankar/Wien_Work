from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('order/<int:pk>', views.customer_order, name='order'),
    path('customer/<int:pk>', views.customer_num, name='customer'),
    path('delete_details/<int:pk>', views.delete_details, name='delete_details'),
    path('add_details/', views.add_details, name = 'add_details'),
    path('update_details/<int:pk>', views.update_details, name='update_details'),
]

