from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    #path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'),
    path('order/<int:pk>', views.customer_order, name='order'),
    path('customer/<int:pk>', views.customer_num, name='customer'),
]

