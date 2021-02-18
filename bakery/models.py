from django.db import models

class Units(models.Model):
    name = models.CharField(max_length=20, unique=True)
    symbol = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    name = models.CharField(max_length=20, unique=True)
    price = models.FloatField()

    def __str__(self):
        return self.name

class BakeryItems(models.Model):
    name = models.CharField(max_length=20, unique=True)
    ingredients = models.ManyToManyField(
                                        Ingredients, 
                                        through='Composition',
                                        through_fields=('bakeryItem', 'ingredients')
                                        )
    profit = models.FloatField()
    discount = models.FloatField()

    def __str__(self):
        return self.name

class Composition(models.Model):
    bakeryItem = models.ForeignKey(BakeryItems, on_delete=models.CASCADE)
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()
    units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True, unique=False)

    class Meta:
        unique_together = [['bakeryItem', 'ingredients']]

    def __str__(self):
        return str(self.quantity)

'''
Models for inventory management
'''

class RawMaterials(models.Model):
    ingredients = models.ForeignKey(Ingredients, related_name='amount', on_delete=models.CASCADE)
    quantity = models.FloatField()
    units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.quantity)

class EndProducts(models.Model):
    bakeryItems = models.ForeignKey(BakeryItems, related_name='amount' , on_delete=models.CASCADE)
    quantity = models.FloatField()
    units = models.ForeignKey(Units, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.quantity)