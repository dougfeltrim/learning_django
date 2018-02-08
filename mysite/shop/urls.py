from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [

    path('', views.index, name='index'),
    path('<int:sell_id>/detail/', views.detail, name='detail'),
    path('<int:sell_id>/results/', views.results, name='results'),
    path('<int:sell_id>/price/', views.price, name='price'),
    path('<int:sell_id>/amount/', views.amount, name='amount'),
]
