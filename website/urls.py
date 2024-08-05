from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('customer/<int:pk>/', views.customer_order, name='customer_order'),
    path('order/<int:pk>/', views.customer_order, name='customer_order'),
    path('customer/<int:pk>', views.customer_num, name='customer_num'),
    path('delete_CustomerDetails/<int:pk>', views.delete_CustomerDetails, name='delete_CustomerDetails'),
    path('add_CustomerDetails/', views.add_CustomerDetails, name = 'add_CustomerDetails'),
    path('about/', views.about, name = 'about'),
    path('update_CustomerDetails/<int:pk>', views.update_CustomerDetails, name='update_CustomerDetails'),
    path('add_OrderDetails/', views.add_OrderDetails, name = 'add_OrderDetails'),
    path('delete_OrderDetails/<int:pk>/', views.delete_OrderDetails, name = 'delete_OrderDetails'),
    path('update_OrderDetails/', views.update_OrderDetails, name = 'update_OrderDetails'),
    path('order_Details/<int:pk>', views.order_Details, name = 'order_Details'),
    path('update_order_status/<int:pk>/', views.update_order_status, name='update_order_status'), 
]