from django.contrib import admin
from bakery.models import Units, Ingredients, BakeryItems, Composition, RawMaterials, EndProducts

class UnitsAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Units, UnitsAdmin)

class BakeryItemsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profit', 'discount')

admin.site.register(BakeryItems, BakeryItemsAdmin)

class IngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Ingredients, IngredientsAdmin)

class CompositionAdmin(admin.ModelAdmin):
    list_display = ('bakeryItem', 'ingredients', 'quantity', 'units')

admin.site.register(Composition, CompositionAdmin)

class RawMaterialsAdmin(admin.ModelAdmin):
    list_display = ('ingredients', 'quantity', 'units')

admin.site.register(RawMaterials, RawMaterialsAdmin)

class EndProductsAdmin(admin.ModelAdmin):
    list_display = ('bakeryItems', 'quantity', 'units')

admin.site.register(EndProducts, EndProductsAdmin)
