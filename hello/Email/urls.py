from django.urls import path
from Email import  views

urlpatterns = [
    path('SendMessage/<str:cedula>/<str:nombre>/<str:asesor>/<str:correo>/<int:tipo>', views.EmailPropia.as_view(), name='EmailPropia'),
    path('Trap/<str:nombre>/<str:monto>/<str:fecha>/<str:mail>/<str:cc>/<str:phone>/<str:agent>/<str:codemp>/<str:destino>'
    , views.EmailTrap.as_view(), name='PSE'),
]