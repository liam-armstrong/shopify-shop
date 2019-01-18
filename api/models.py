from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    inventory_count = models.IntegerField()

    def purchase(self):
        if self.inventory_count < 1: 
            raise ValueError
        self.inventory_count -= 1 #updates inventory count
        self.save(update_fields=["inventory_count"], force_update=True) #saves updated field
    
    def __str__(self):
        return self.title