from django.shortcuts import render
from .models import Product, Appointment, Cart
from .serializers import ProductSerializer, AppointmentSerializer, CartSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response

# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [AllowAny]


class ProductDetail(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs.get('pk'))


class PetFoodList(ListCreateAPIView):
    queryset = Product.objects.filter(category='healthcare')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class PetMedicineList(ListCreateAPIView):
    queryset = Product.objects.filter(category='medicine')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class PetParlourList(ListCreateAPIView):
    queryset = Product.objects.filter(category='parlour')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class PetAccessoriesList(ListCreateAPIView):
    queryset = Product.objects.filter(category='accessories')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class AppointmentList(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [AllowAny]


class CartList(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]

    
    def get_queryset(self):
        username = self.kwargs['username']
        user_obj = get_user_model().objects.filter(username=username).first()
        cart_obj = Cart.objects.filter(user = user_obj)
        return cart_obj

    def post(self, request, username):
        name = request.data.get('name')
        price = request.data.get('price')
        category = request.data.get('category')
        description = request.data.get('description')
        image = request.data.get('image')
        user_obj = get_user_model().objects.get(username=username)

        if(Cart.objects.filter(name=name).count()):
            Cart.objects.filter(name=name).delete()
        else:
            Cart.objects.create(name=name, price=price, category=category, description=description, image=image, user=user_obj)
        
        return Response(status.HTTP_201_CREATED)


