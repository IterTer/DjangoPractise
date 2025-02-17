from django.urls import path

from . import views

# homepage
urlpatterns = [
    path('', views.index, name='index')
]