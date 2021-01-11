from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
app_name='dash'
urlpatterns=[
    path('',views.home,name='main'),
    path('products/',views.products,name='products'),
    path('features/',views.Feature.as_view(),name='features'),
    path('product/<int:pk>',views.ProductDetailView.as_view(),name='product'),
    path('product/<int:pk>/delete',views.ProductDeleteView.as_view(),name='product_delete'),
    path('registration/', views.Register.as_view(),name='registration'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('customer/<int:pk>/',views.customer,name='customer'),
    path('create_order/<int:pk>/',views.createOrder,name='create_order'),
    path('update_order/<int:pk>/',views.updateOrder, name='update_order'),
    path('delete_order/<int:pk>/', views.deleteOrder, name='delete_order'),
    path('user_page/', views.userPage, name='user_page'),
    path('account/', views.accountSettings, name='account_settings'),
    path('shop/', views.shop, name='shopping'),
    path('order/<int:pk>', views.order, name='order'),
    path('order_done/', views.orderDone, name='order_done'),
    path('order_detail/<int:pk>/', views.orderDetail, name='order_detail'),
    path('myorders', views.allCustomerOrders, name='myorders'),
]
