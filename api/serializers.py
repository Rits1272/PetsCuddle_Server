from rest_framework.serializers import ModelSerializer
from .models import Product, Appointment, Cart, Profile


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


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

