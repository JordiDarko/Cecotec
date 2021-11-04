from django.urls import path
from app1 import views

urlpatterns = [
    path('product_list/', views.product_list),
    path('order_list/', views.order_list),
    path('order/<int:id>/', views.order),
    path('add_order/', views.add_order),
    path('add_item/', views.add_item),
]
