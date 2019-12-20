from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny

# Create your views here.
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    permission_classes = [AllowAny]


