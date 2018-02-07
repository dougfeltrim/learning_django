from django.urls import path

from . import views

app_name = 'shop'
urlpatterns = [

    path('', views.index, name='index'),
    path('detail/<int:sell_id>/', views.detail, name='detail'),
    path('results/<int:sell_id>/', views.results, name='results'),
    path('price/<int:sell_id>/', views.price, name='price'),
    path('amount/<int:sell_id>/', views.amount, name='amount'),
]
