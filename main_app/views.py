from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Cars
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

# Views for Make
class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query for search button
        make =self.request.GET.get("make")
        if make != None:
            context["carss"] = Cars.objects.filter(make__icontains=make)
        else:    
            context["carss"] = Cars.objects.all()
            # default header
            context["header"] = "Cars Make"
        return context

class CarsCreate(CreateView):
    model = Cars
    fields = ['make', 'img', 'country']
    template_name = "cars_create.html"
    success_url = "/cars/"

class CarsDetail(DeleteView):
    model = Cars
    template_name = "cars_detail.html"