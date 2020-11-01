from django.urls import path
from . import views

app_name='dash'
urlpatterns=[
    path('',views.HomeView.as_view(),name='main'),
    path('products/',views.products,name='products'),
    path('features/',views.Feature.as_view(),name='features'),
    path('product/<int:pk>',views.ProductDetailView.as_view(),name='product'),
    path('product/<int:pk>/delete',views.ProductDeleteView.as_view(),name='product_delete'),
    path('registration/',views.Register.as_view(),name='registration'),

]