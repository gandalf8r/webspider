from email.policy import default
from enum import unique
from django.db import models


class Car(models.Model):
    url = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    price_usd = models.IntegerField()
    otometer = models.IntegerField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    image_url = models.ImageField()
    images_count = models.IntegerField()
    car_number = models.CharField(max_length=255, null=True)
    car_vin = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

