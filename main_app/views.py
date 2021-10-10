from django.shortcuts import  redirect, render
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from .models import Cars, Model, Favorite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse


# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["favorites"] = Favorite.objects.all()
    #     return context




# Views for Cars
class CarsList(TemplateView):
    template_name = "cars_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # query for search button
        make =self.request.GET.get("make")
        if make != None:
            context["carss"] = Cars.objects.filter(make__icontains=make, user=self.request.user)
            context["header"] = f"Searching for {make}"
        else:    
            context["carss"] = Cars.objects.filter(user=self.request.user)
            # default header
            context["header"] = "Cars Make"
        return context

class CarsCreate(CreateView):
    model = Cars
    fields = ['make', 'img', 'country']
    template_name = "cars_create.html"
    # success_url = "/cars/"
    # to redirect to cars detail

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CarsCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('cars_detail', kwargs={'pk': self.object.pk})

class CarsDetail(DetailView):
    model = Cars
    template_name = "cars_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context



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

# views for Favorite
class Fav(TemplateView):
    template_name = "favorite.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["favorites"] = Favorite.objects.all()
        return context

class FavoriteModelAssoc(View):
    def get(self, request, pk, model_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Favorite.objects.get(pk=pk).models.remove(model_pk)
        if assoc == "add":
            Favorite.objects.get(pk=pk).models.add(model_pk)
        return redirect('favorite')        
