from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Cars

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

# Views for Make
class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["carss"] = Cars.objects.all()
        return context