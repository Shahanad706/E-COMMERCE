from django.urls import path
from . import views

urlpatterns = [
    path('/cartdetails',views.cartdetails,name='cartdetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('decrement/<int:product_id>/',views.decrement_cart,name='decrementcart'),
    path('delete/<int:product_id>/',views.delete_cart,name='deletecart'),
]