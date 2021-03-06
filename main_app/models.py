from django.db import models
from django.contrib.auth.models import User
# import datetime
# from partial_date import PartialDate
# from django_countries.fields import CountryField


# Create your models here.
class Cars(models.Model):
    make = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    # country = CountryField(blank_label='(select country)')
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    # User auth
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.make

    class Meta:
        ordering = ['make']    

class Model(models.Model):
    type = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    year = models.CharField(max_length=4)
    # year = partial_date_instance.precisionYear()
    cars = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return self.type

class Favorite(models.Model):
    person = models.CharField(max_length=50)
    models = models.ManyToManyField(Model)

    def __str__(self):
        return self.person        