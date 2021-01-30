from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.http import JsonResponse
import pandas as pd
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class EmailPropia(APIView):
    def post(self, request, *args, **kwargs):
        
        if self.kwargs['tipo'] == 0:
            subject = 'Cartera Propia - Solicitud Paz y Salvo'
            solicitud = 'de paz y salvo'
        elif self.kwargs['tipo'] == 1:
            subject = 'Cartera Propia - Solicitud Certificado Deuda'
            solicitud = 'certificado de deuda'
        else:
            return Response({'error':'opción de mensaje invalida'}, status=status.HTTP_400_BAD_REQUEST)
        
        text = """
Cordial saludo


Se solicita {3} para el deudor {0}, con CC {1}, el cual fue gestionando por {2}.
Favor enviar a {4}


Gracias por su colaboración
        """
        mail = send_mail(
            subject,
            text.format(
                self.kwargs['nombre'],
                self.kwargs['cedula'],
                self.kwargs['asesor'],
                solicitud,
                self.kwargs['correo'],
                ),
            'carterarecuperacion@cobrando.com.co',
            [
                # 'Administraciondecartera@cobrando.com.co',
                # 'larodriguez@cobrando.com.co'
                # 'mgonzalez@cobrando.com.co',
                # 'desarrollo@cobrando.com.co',
                # 'vallonmar@gmail.com',
                'manuel_perez_32@outlook.com'
            ],
            fail_silently=False)
        
        if mail == 1:
            return Response({'estado':'correo enviado'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'no se envio el mensaje'}, status=status.HTTP_400_BAD_REQUEST)

class EmailTrap(APIView):
    def post(self, request, *args, **kwargs):
        
        html_message = render_to_string('trap.html', {'context': 'values'})
        plain_message = strip_tags(html_message)
        subject = 'Pago PSE'
        mail = send_mail(
            subject,
            plain_message,
            'carterarecuperacion@cobrando.com.co',
            [
                # 'Administraciondecartera@cobrando.com.co',
                # 'larodriguez@cobrando.com.co'
                # 'mgonzalez@cobrando.com.co',
                # 'desarrollo@cobrando.com.co',
                # 'vallonmar@gmail.com',
                'manuel_perez_32@outlook.com'
            ],
            fail_silently=False,
            html_message=html_message)
        
        if mail == 1:
            return Response({'estado':'correo enviado'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'no se envio el mensaje'}, status=status.HTTP_400_BAD_REQUEST)