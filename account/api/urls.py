from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from account.api.views import (
    user_details, 
    registration, 
    get_product_list,
    place_order,
    get_order_history,
    get_bill
)

app_name = 'account'

urlpatterns = [
    path('register/', registration, name='registration'),
    path('login/', obtain_auth_token, name='login'),
    path('get-product-list/', get_product_list, name='get-product-list'),
    path('place-order/', place_order, name='place-order'),
    path('get-order-history/', get_order_history, name='get-order-history'),
    path('get-bill/<id>', get_bill, name='get-bill'),
    path('user-details/', user_details, name='details'),
]