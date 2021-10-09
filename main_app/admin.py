from django.contrib import admin
from .models import Cars, Model, Favorite
# Register your models here.

admin.site.register(Cars)
admin.site.register(Model)
admin.site.register(Favorite)