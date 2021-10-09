from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name="home"),
#    Cars  urls
   path('cars/', views.CarsList.as_view(), name="cars_list"),
   path('cars/new', views.CarsCreate.as_view(), name="cars_create"),
   path('cars/<int:pk>/', views.CarsDetail.as_view(), name="cars_detail"),
   path('cars/<int:pk>/update', views.CarsUpdate.as_view(), name="cars_update"),
   path('cars/<int:pk>/delete', views.CarsDelete.as_view(), name="cars_delete"),
#  Models url
   path('cars/<int:pk>/models/new/', views.ModelCreate.as_view(), name="model_create"),
   
   
]