from django.urls import path
from Email import  views

urlpatterns = [
    path('SendMessage/<str:cedula>/<str:nombre>/<str:asesor>/<str:correo>/<int:tipo>', views.EmailPropia.as_view(), name='EmailPropia'),
    path('Trap/', views.EmailTrap.as_view(), name='PSE'),
]