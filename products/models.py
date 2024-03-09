from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, db_default=99.99)

    def __str__(self):
        return self.title

    @property
    def sale_price(self):
        return "{:.2f}".format(self.price)

    def get_discount(self):
        return "122.20"

# Create your models here.
