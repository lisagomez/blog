from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="inv-home"),
    path('about/', views.about, name="inv-about"),
]

