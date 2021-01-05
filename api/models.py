from django.db import models
import os 
from uuid import uuid4
from petApi import settings
from django.contrib.auth import get_user_model
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_SID = os.getenv('ACCOUNT_SID')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')


def photo_path(instance, filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    
    return os.path.join(upload_to, filename)


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
    image = models.ImageField(upload_to=photo_path)
    category = models.CharField(max_length=15, 
                                choices=category_choices, 
                                default='healthcare')

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name 


class Appointment(models.Model):
    problem = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    timeslot = models.DateTimeField(null=False)

    def __str__(self):
        return self.problem

    def save(self, *args, **kwargs):
        account_sid = ACCOUNT_SID
        auth_token = AUTH_TOKEN 
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                body = "You have booked your appointment sucessfully on: " + str(self.timeslot),
                from_ = '+12063377761',
                to = '+916264947400'
                )
        print("[LOG] Message send succesfully!")
        return super().save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    price = models.IntegerField(null=False)
    category = models.CharField(max_length=50)
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    pincode = models.CharField(max_length=10, null=False)
    first_line = models.CharField(max_length=100, null=False)
    second_line = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=15, null=False)
    email = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.user.username
