from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    p_id = models.CharField(max_length=10, primary_key=True)
    p_name = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.URLField()
    slug = models.SlugField(max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def is_out_of_stock(self):
        return (self.stock>0)

    def __str__(self):
        return self.p_name