from django.urls import path
from . import views

urlpatterns = [
    # path('', views.getData),
    path('Origen1', views.add1),
    path('Origen2', views.add2)
]
