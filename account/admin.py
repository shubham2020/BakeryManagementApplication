from django.contrib import admin
from account.models import Orders, OrderedItems

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')

admin.site.register(Orders, OrdersAdmin)

class OrderedItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'item', 'quantity')

admin.site.register(OrderedItems, OrderedItemsAdmin)

