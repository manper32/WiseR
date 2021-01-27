from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
import pandas as pd
import mysql.connector
import requests
import time

def ED_Vici(AgentUser,Phone,VendorId,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'agc',
        'user' : 'soporte',
        'psw' : 'Bogota1234'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'agc',
        'user' : 'secetina',
        'psw' : '1233692646'}

    # url
    # with open(r"/home/manuel/Documentos/WiseR/Vicidial/Templates/ED_URL.txt","r") as f1:
    ed_url = ' http://{0}/{1}/api.php?source=test&user={2}&pass={3}&agent_user={4}&function=external_dial&value={5}&vendor_id={6}&phone_code=1&search=NO&preview=NO&focus=NO'
        
    b = requests.get(ed_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    AgentUser,
                                    Phone,
                                    VendorId)).text.split('|')
                       # ,columns= ['status',
                                  # 'list_id',
                                  # 'list_name',
                                  # 'campaign_id'])

    return b

def EH_Vici(user,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'agc',
        'user' : 'soporte',
        'psw' : 'Bogota1234'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'agc',
        'user' : 'secetina',
        'psw' : '1233692646'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/EH_URL.txt","r") as f1:
    eh_url = 'http://{0}/{1}/api.php?source=test&user={2}&pass={3}&agent_user={4}&function=external_hangup&value=1'
        
    b = requests.get(eh_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    user)).text.split('|')

    return b

def EP_Vici(user,value,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'agc',
        'user' : 'soporte',
        'psw' : 'Bogota1234'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'agc',
        'user' : 'secetina',
        'psw' : '1233692646'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/EP_URL.txt","r") as f1:
    ep_url = 'http://{0}/{1}/api.php?source=test&user={2}&pass={3}&agent_user={4}&function=external_pause&value={5}'
        
    b = requests.get(ep_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    user,
                                    value)).text.split('|')

    return b

def ES_Vici(user,status,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'agc',
        'user' : 'soporte',
        'psw' : 'Bogota1234'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'agc',
        'user' : 'secetina',
        'psw' : '1233692646'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/ES_URL.txt","r") as f1:
    es_url = 'http://{0}/{1}/api.php?source=test&user={2}&pass={3}&agent_user={4}&function=external_status&value={5}'
        
    b = requests.get(es_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    user,
                                    status)).text.split('|')

    return b

def PC_Vici(user,value,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'agc',
        'user' : 'soporte',
        'psw' : 'Bogota1234'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'agc',
        'user' : 'secetina',
        'psw' : '1233692646'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/PC_URL.txt","r") as f1:
    pc_url = 'http://{0}/{1}/api.php?source=test&user={2}&pass={3}&agent_user={4}&function=pause_code&value={5}'
        
    b = requests.get(pc_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    user,
                                    value)).text.split('|')

    return b
    
def CI_Vici(user,ingroup,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip
        }
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip
        }

    ci_url = 'http://{0}/agc/api.php'
    args1 = {
        'source':'test',
        'user':'secetina',
        'pass':'1233692646',
        'agent_user':user,
        'function':'change_ingroups',
        'value':'CHANGE',
        'set_as_default':'YES',
        'blended':'YES',
        'ingroup_choices':ingroup
    }
    
    args2 = {
        'source':'test',
        'user':'secetina',
        'pass':'1233692646',
        'agent_user':user,
        'function':'logout',
        'value':'LOGOUT',
    }
    
    b = requests.get(ci_url.format(connV.get('server'))
                     ,params=args1).text.split('|')
    l = requests.get(ci_url.format(connV.get('server'))
                     ,params=args2).text.split('|')

    return [b,l]

class Dial(APIView):
    def post(self, request, *args, **kwargs):
        a = ED_Vici(self.kwargs['AgentUser'],self.kwargs['Phone'],self.kwargs['VendorId'],self.kwargs['numip'])
        if a[0].find('ÉXITO: conjunto de funciones external_dial') > -1:
            return Response({'result' : a[0]},status = status.HTTP_200_OK)
        else:
            return Response({'result' : a[0]},status = status.HTTP_400_BAD_REQUEST)

class HangUp(APIView):
    def post(self, request, *args, **kwargs):
        a = EH_Vici(self.kwargs['user'],self.kwargs['numip'])
        if a[0].find('ÉXITO: conjunto de funciones external_hangup') > -1:
            return Response({'result' : a[0]},status = status.HTTP_200_OK)
        else:
            return Response({'result' : a[0]},status = status.HTTP_400_BAD_REQUEST)

class Pause(APIView):
    def post(self, request, *args, **kwargs):
        a = EP_Vici(self.kwargs['user'],self.kwargs['value'],self.kwargs['numip'])
        if a[0].find('ÉXITO: conjunto de funciones external_pause') > -1:
            return Response({'result' : a[0]},status = status.HTTP_200_OK)
        else:
            return Response({'result' : a[0]},status = status.HTTP_400_BAD_REQUEST)

class Status(APIView):
    def post(self, request, *args, **kwargs):
        a = ES_Vici(self.kwargs['user'],self.kwargs['status'],self.kwargs['numip'])
        if a[0].find('ÉXITO: conjunto de funciones external_status') > -1:
            return Response({'result' : a[0]},status = status.HTTP_200_OK)
        else:
            return Response({'result' : a[0]},status = status.HTTP_400_BAD_REQUEST)

class PauseCode(APIView):
    def post(self, request, *args, **kwargs):
        a = PC_Vici(self.kwargs['user'],self.kwargs['value'],self.kwargs['numip'])
        if a[0].find('ÉXITO: función pause_code envió') > -1:
            return Response({'result' : a[0]},status = status.HTTP_200_OK)
        else:
            return Response({'result' : a[0]},status = status.HTTP_400_BAD_REQUEST)

class HangUpManual(APIView):
    def post(self, request, *args, **kwargs):
        a = EH_Vici(self.kwargs['user'],self.kwargs['numip'])
        c = ES_Vici(self.kwargs['user'],self.kwargs['status'],self.kwargs['numip'])
        time.sleep(2)
        b = EP_Vici(self.kwargs['user'],'PAUSE',self.kwargs['numip'])
        time.sleep(2)
        d = PC_Vici(self.kwargs['user'],self.kwargs['value'],self.kwargs['numip'])
        if a[0].find('ÉXITO:') > -1\
        and c[0].find('ÉXITO:') > -1\
        and b[0].find('ÉXITO:') > -1\
        and d[0].find('ÉXITO:') > -1:
            return Response({
                'result hangup' : a[0],
                'result status' : c[0],
                'result pause' : b[0],
                'resut pause_code': d[0]
            },status = status.HTTP_200_OK)
        else:
            return Response({
                'result hangup' : a[0],
                'result status' : c[0],
                'result pause' : b[0],
                'resut pause_code' : d[0]
            },status = status.HTTP_400_BAD_REQUEST)

class ChangeIngroups(APIView):
    def post(self, request, *args, **kwargs):
        #credenciales MySQL120
        connM = {
            'host' : '10.152.1.'+self.kwargs['numip'],
            'user':'desarrollo',
            'password':'soportE*8994',
            'database' : 'asterisk'}

        query = """
        select closer_campaigns
        from asterisk.vicidial_users
        where user = '{0}';"""

        ingroup = pd.read_sql(query.format(self.kwargs['user']),mysql.connector.connect(**connM)).iloc[0,0]

        a = CI_Vici(self.kwargs['user'],ingroup,self.kwargs['numip'])
        if a[0][0].find('ÉXITO:') > -1 and a[1][0].find('ÉXITO:') > -1:
            return Response({
                'change_ingroups' : a[0][0],
                'logout' : a[1][0]
            },status = status.HTTP_200_OK)
        else:
            return Response({
                'change_ingroups' : a[0][0],
                'logout' : a[1][0]
            },status = status.HTTP_400_BAD_REQUEST)