from rest_framework.serializers import ModelSerializer
from .models import Product, Appointment, Cart


class ProductSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Product


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
