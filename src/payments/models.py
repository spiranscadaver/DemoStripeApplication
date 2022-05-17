from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}$"
