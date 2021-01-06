from django.contrib import admin
from .models import Product, Appointment, Cart, Profile, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(Appointment)
admin.site.register(Cart)
admin.site.register(Profile)
admin.site.register(Order)

