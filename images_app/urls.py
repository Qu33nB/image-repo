from django.urls import path
from images_app import views

urlpatterns = [ path('', views.index, name = 'home')]
