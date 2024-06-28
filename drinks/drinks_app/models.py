from django.db import models

class Drinks(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
