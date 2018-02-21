from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:local_id>/detail/', views.detail, name='detail'),
    path('<int:local_id>/cep/', views.cep, name='cep'),
    #path('int:local_id/display_all/', views.display_all, name='display_all')
]
