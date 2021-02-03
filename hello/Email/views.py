from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.http import JsonResponse
from django.http import HttpResponseRedirect
import pandas as pd
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import requests

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
                'Administraciondecartera@cobrando.com.co',
                'larodriguez@cobrando.com.co'
                # 'mgonzalez@cobrando.com.co',
                # 'desarrollo@cobrando.com.co',
                # 'vallonmar@gmail.com',
                # 'manuel_perez_32@outlook.com'
            ],
            fail_silently=False)
        
        if mail == 1:
            return Response({'estado':'correo enviado'}, status=status.HTTP_200_OK)
        else:
            return Response({'error':'no se envio el mensaje'}, status=status.HTTP_400_BAD_REQUEST)

class EmailTrap(APIView):
    def post(self, request, *args, **kwargs):
        
        url = 'https://www.carteraok.com/pagos/psecreate'
        token = '7add33098bfadd20260e19945b64ed4acfa52d48'
        args = {
            "total_with_iva":self.kwargs['monto'],
            "value_iva":0,
            "description_payment":"acuerdo de pago No.",
            "email":self.kwargs['mail'],
            "id_client":self.kwargs['cc'],
            "name_client":self.kwargs['nombre'],
            "lastname_client":"N/A",
            "phone_client":self.kwargs['phone'],
            "info_optional1":"",
            "info_optional2":"",
            "identity_agent":self.kwargs['agent'],
            "codemp":self.kwargs['codemp'],
            "token":token,
        }
        response = requests.post(url,
        headers={'Authorization':'7add33098bfadd20260e19945b64ed4acfa52d48'},
        json=args)
        # print(response.json())
        
        html_message = render_to_string('new-trap.html', {
            'Nombrecliente': self.kwargs['nombre'],
            'Monto':self.kwargs['monto'],
            'Fechapago':self.kwargs['fecha'],
            'URL':response.json().get('link'),
            })
        plain_message = strip_tags(html_message)
        subject = 'Acuerdo de pago - Cobrando BPO'

        
        mail = EmailMultiAlternatives(
        subject,
        plain_message,
        'carterarecuperacion@cobrando.com.co',
        [
            self.kwargs['destino'],
        ])
        mail.attach_alternative(html_message, 'text/html')
        mail.send()

        
        # if mail == 1:
        return Response({'estado':'correo enviado'}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'error':'no se envio el mensaje'}, status=status.HTTP_400_BAD_REQUEST)