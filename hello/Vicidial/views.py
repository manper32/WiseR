from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse
from Vicidial.models import VicidialStatusValidator
import pandas as pd
import mysql.connector
import requests
import time
import json

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
        'server' : '10.150.1.'+numip,
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
        'server' : '10.150.1.'+numip,
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
        'server' : '10.150.1.'+numip,
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
        'server' : '10.150.1.'+numip,
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
        'server' : '10.150.1.'+numip,
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
        'server' : '10.150.1.'+numip
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

def AU_Vici(a_user,a_pswd,u_level,full_name,u_group,numip):

    connV = {
    'server' : '10.150.1.'+numip,
    'agc' : 'vicidial',
    'user' : 'secetina',
    'psw' : '1233692646'}

    # # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/AU_URL.txt","r") as f1:
    #     au_url = f1.read()
    au_url = 'http://{0}/{1}/non_agent_api.php?source=test&function=add_user&user={2}&pass={3}&agent_user={4}&agent_pass={5}&agent_user_level={6}&agent_full_name={7}&agent_user_group={8}'
        
    b = requests.get(au_url.format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    a_user,
                                    a_pswd,
                                    u_level,
                                    full_name,
                                    u_group)).text.split('|')

    return b

#######################################

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
            'host' : '10.150.1.'+self.kwargs['numip'],
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

class AddUser(APIView):
    def post(self, request, *args, **kwargs):
        
        a = AU_Vici(
            self.kwargs['user'],
            self.kwargs['psw'],
            self.kwargs['level'],
            self.kwargs['full_name'],
            self.kwargs['group'],
            self.kwargs['numip'])
        # SUCCESS: add_user USER HAS BEEN ADDED - soporte
        if a[0].find('SUCCESS:') > -1:
            return Response({
                'AddUser' : a[0]
            },status = status.HTTP_200_OK)
        else:
            return Response({
                'AddUser' : a[0]
            },status = status.HTTP_400_BAD_REQUEST)

class AgentStatus(APIView):
    def get(self, request, *args, **kwargs):
        # credentials Vicidial
        connV = {
            'server' : '10.150.1.'+self.kwargs['numip'],
            'agc' : 'vicidial',
            'user' : 'secetina',
            'psw' : '1233692646'
        }
        url='http://{0}/{1}/non_agent_api.php'
        args = {
          'source':'test',
          'user':connV.get('user'),
          'pass':connV.get('psw'),
          'function':'agent_status',
          'agent_user':self.kwargs['user'],
          'header':'NO'
        }
        a = requests.get(url.format(connV.get('server')
                                ,connV.get('agc'))
                    ,params=args).text.split('|')
        # print(a)

        if requests.get(url.format(connV.get('server'),connV.get('agc')),params=args).status_code < 300:
            b = pd.DataFrame([a],columns= ['status',
                                            'call_id',
                                            'lead_id',
                                            'campaign_id',
                                            'calls_today',
                                            'full_name',
                                            'user_group',
                                            'user_level',
                                            'pause_code',
                                            'real_time_sub_status',
                                            'phone_number',
                                            'vendor_lead_code',
                                            'session_id']).to_json(orient='records')
            return JsonResponse(json.loads(b),safe=False)
        else:
            return Response({
                'AgentStatus' : a[0]
            },status = status.HTTP_400_BAD_REQUEST)

# consulta validacion de telefonos
class ConsultaVicidialStatusValidator(APIView):
    def get(self, request, *args, **kwargs):
        #credenciales MySQL206
        connM = {
            'host' : '10.150.1.206',
            'user':'desarrollo',
            'password':'soportE*8994',
            'database' : 'asterisk'
            }
        #query PostgreSQL
        query ="""
select substring(phone_number from 2 for 11)phone_number, vendor_lead_code, status, count(*) cantidad
from asterisk.vicidial_list
WHERE list_id = 20200811001
AND CAST(modify_date as date) = '{0}'
and SUBSTRING(phone_number from 1 for 1) = '9'
and length(phone_number) = 11
group by vendor_lead_code,substring(phone_number from 2 for 1),status
order by vendor_lead_code,substring(phone_number from 2 for 1),status desc;
        """
        # print(pd.read_sql(query,mysql.connector.Connect(**connM)))
        # print(pd.DataFrame(list(VicidialStatusValidator.objects.using('public').all().values())))
        b = pd.merge(pd.read_sql(query.format(self.kwargs['fecha']),mysql.connector.Connect(**connM))
                ,pd.DataFrame(list(VicidialStatusValidator.objects.using('public').all().values()))
                ,how = 'left'
                ,on = 'status'
                ,indicator=False).to_json(orient='records')
        
        return JsonResponse(json.loads(b),safe=False)
        # return Response({'AddUser' : 'ok'},status = status.HTTP_200_OK)

# consulta indicadores de tareas
class VicidialListIndicators(APIView):
    def get(self, request, *args, **kwargs):
        #credenciales MySQL120
        connM = {
            'host' : '10.150.1.'+self.kwargs['numip'],
            'user':'desarrollo',
            'password':'soportE*8994',
            'database' : 'asterisk'
        }
        query = """SELECT
t2.list_name
,t1.list_id
,sum(case when t1.status in ('MS','SMS','NE''NC','BZ','MST','CO','PSC','FLL','FL','ME','FAS','TRA','PU','NC') then 1 else 0 end ) no_contacto
,sum(case when t1.status in ('PS','PSC') then 1 else 0 end ) presion
,sum(case when t1.status in ('SG') then 1 else 0 end ) seguimiento
,sum(case when t1.status in ('CP','CR') then 1 else 0 end ) compromiso
,sum(case when t1.status in ('NG') then 1 else 0 end ) negociacion 
FROM asterisk.vicidial_list t1
left join asterisk.vicidial_lists t2
on t1.list_id = t2.list_id 
-- where t1.list_id = 29012021123456;
-- WHERE t2.list_name = 'ADELANTOS NVO 2901'
where CAST(t1.modify_date as date) >= SUBDATE(CURRENT_DATE(), DAYOFMONTH(CURRENT_DATE()) - 1)
GROUP by t1.list_id
order by t1.list_id;
        """
        b = pd.read_sql(query,mysql.connector.Connect(**connM)).to_json(orient='records')
        return JsonResponse(json.loads(b),safe=False)