from django.db import models
# from django_countries.Field import CountryField


# Create your models here.
class Cars(models.Model):
    make = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    # country = CountryField()
    country = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.make
