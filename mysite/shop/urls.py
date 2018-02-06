from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:sell_id>/', views.detail, name='detail'),
    path('<int:sell_id>/', views.results, name='results'),
    path('<int:sell_id>/', views.price, name='price'),
    path('<int:sell_id>/', views.amount, name='amount'),
]
