from django.urls import path
from bakery.api.views import (
    get_bakery_item, 
    add_ingredient, 
    add_bakery_item, 
    add_raw_material,
    get_raw_material,
    add_end_product,
    get_end_product
)

app_name = 'bakery'

urlpatterns = [
    path('get-bakery-item/<id>', get_bakery_item, name='get-bakery-item'),
    path('add-bakery-item/', add_bakery_item, name='add-bakery-item'),
    path('add-ingredient/', add_ingredient, name='add-ingredient'),
    path('add-raw-material/', add_raw_material, name='add-raw-material'),
    path('get-raw-material/<id>', get_raw_material, name='get-raw-material'),
    path('add-end-product/', add_end_product, name='add-end-product'),
    path('get-end-product/<id>', get_end_product, name='get-end-product'),
]