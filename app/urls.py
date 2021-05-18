from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('temp/c_to_f', views.celciusTOfahrenheit, name='c-to-f'),
    path('temp/f-to-c', views.fahrenheitTOcelcius, name='f-to-c')
]
