from django.contrib import admin
from .models import Product, Appointment, Cart

# Register your models here.
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Cart)
