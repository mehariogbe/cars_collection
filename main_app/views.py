from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Cars, Model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

# Views for Cars
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
    # success_url = "/cars/"
    # to redirect to cars detail
    def get_success_url(self):
        return reverse('cars_detail', kwargs={'pk': self.object.pk})

class CarsDetail(DetailView):
    model = Cars
    template_name = "cars_detail.html"

class CarsUpdate(UpdateView):
    model = Cars
    fields = ['make', 'img', 'country']
    template_name = "cars_update.html"
    # success_url = "/cars/"
    # to redirect to cars detail
    def get_success_url(self):
        return reverse('cars_detail', kwargs={'pk': self.object.pk})

class CarsDelete(DeleteView):
    model = Cars
    template_name = "cars_delete_confirm.html"
    success_url = "/cars/"
     
# views for Model
class ModelCreate(View):
    def post(self, request, pk):
        type = request.POST.get("type")
        img = request.POST.get("img")
        year = request.POST.get("year")
        cars = Cars.objects.get(pk=pk)
        Model.objects.create(type=type, img=img, year=year, cars=cars)
        return redirect('cars_detail', pk=pk)
         