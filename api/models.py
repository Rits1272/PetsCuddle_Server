from django.db import models

# Create your models here.
class Product(models.Model):

    category_choices = [
        ('medicine', 'Medicine'),
        ('parlour', 'Parlour'),
        ('accessories', 'Accessories'),
        ('healthcare', 'HealthCare'),
    ]

    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    qty = models.IntegerField(null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=15, 
                                choices=category_choices, 
                                default='healthcare')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name 