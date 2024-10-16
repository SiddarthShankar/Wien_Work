from django.urls import path
from . import views
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('customer/<int:pk>/', views.customer_order, name='customer_order'),
    path('order/<int:pk>/', views.customer_order, name='customer_order'),
    path('customer/<int:pk>', views.customer_num, name='customer_num'),
    path('delete_CustomerDetails/<int:pk>', views.delete_CustomerDetails, name='delete_CustomerDetails'),
    path('add_CustomerDetails/', views.add_CustomerDetails, name='add_CustomerDetails'),
    path('about/', views.about, name='about'),
    path('update_CustomerDetails/<int:pk>', views.update_CustomerDetails, name='update_CustomerDetails'),
    path('add_OrderDetails/', views.add_OrderDetails, name='add_OrderDetails'),
    path('delete_OrderDetails/<int:pk>/', views.delete_OrderDetails, name='delete_OrderDetails'),
    path('update_OrderDetails/<int:pk>/', views.update_OrderDetails, name='update_OrderDetails'),  # Corrected pattern
    path('order_Details/<int:pk>', views.order_Details, name='order_Details'),
    path('update_order_status/<int:pk>/', views.update_order_status, name='update_order_status'),
    path('increase-font-size/', views.increase_font_size, name='increase_font_size'),
    path('decrease-font-size/', views.decrease_font_size, name='decrease_font_size'),
    path('switch-theme/<str:theme_name>/', views.switch_theme, name='switch_theme'), 
    path('set_language/', views.switch_language, name='switch_language'),
]

