from django.shortcuts import render
from .models import Product, Appointment, Cart, Profile
from .serializers import ProductSerializer, AppointmentSerializer, CartSerializer, ProfileSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.response import Response


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [IsAuthenticated]


class ProductDetail(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Product.objects.filter(pk=self.kwargs.get('pk'))


class PetFoodList(ListCreateAPIView):
    queryset = Product.objects.filter(category='healthcare')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class PetMedicineList(ListCreateAPIView):
    queryset = Product.objects.filter(category='medicine')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class PetParlourList(ListCreateAPIView):
    queryset = Product.objects.filter(category='parlour')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class PetAccessoriesList(ListCreateAPIView):
    queryset = Product.objects.filter(category='accessories')
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class AppointmentList(ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsAuthenticated]


class CartList(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        username = self.kwargs['username']
        user_obj = get_user_model().objects.filter(username=username).first()
        cart_obj = Cart.objects.filter(user = user_obj)
        return cart_obj

    def post(self, request, username):
        name = request.data.get('name')

        if(Cart.objects.filter(name=name).count()):
            Cart.objects.filter(name=name).delete()
        else:
            price = request.data.get('price')
            category = request.data.get('category')
            description = request.data.get('description')
            image = request.data.get('image')
            user_obj = get_user_model().objects.get(username=username)
            Cart.objects.create(name=name, price=price, category=category, description=description, image=image, user=user_obj)
        
        return Response(status.HTTP_201_CREATED)


class ProfileList(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        username = self.kwargs['username']
        user_obj = get_user_model().objects.filter(username=username).first()
        return Profile.objects.filter(user = user_obj)


    def post(self, request, username):
        pincode = request.data.get('pincode')
        print(pincode)
        first_line = request.data.get('first_line')
        second_line = request.data.get('second_line')
        phone = request.data.get('phone')
        email = request.data.get('email')        
        user_obj = get_user_model().objects.get(username=username)

        if Profile.objects.filter(user=user_obj).count():
            obj = Profile.objects.get(user=user_obj)
            obj.pincode = pincode
            obj.first_line = first_line
            obj.second_line = second_line
            obj.phone = phone
            obj.email = email
            obj.save()
        else:
            Profile.objects.create(pincode=pincode, first_line=first_line, second_line=second_line, phone=phone, email=email, user=user_obj)

        return Response(status.HTTP_201_CREATED)

