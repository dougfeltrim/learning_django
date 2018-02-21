from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:local_id>/cities/', views.cities, name='cities'),
    path('<int:local_id>/cep/', views.cep, name='cep'),
]
