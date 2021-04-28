from django.contrib import admin
from django.urls import path
from CV import views

urlpatterns = [
    path('ClaroCV/', views.CVClaro.as_view(), name='CV_Claro'),
]