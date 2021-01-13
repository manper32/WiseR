from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from file_app.serializers import FileSerializer, GestionSerializer
from file_app.models import Tipificaciones, Codigos, NombreRama
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from pyexcel_xlsx import get_data
from file_app.models import Gestiones, Tareas, Asignaciones
from datetime import datetime
# from tablib import Dataset 
import jxmlease
import psycopg2
import requests
import pandas as pd
import mysql.connector

cust = [
    'testbogo',
    'testmaf',
    'testok',
    'testclar',
    'testcode',
    'testcolp',
    'testdavi',
    'testfala',
    'testpopu',
    'testprog',
    'testprop',
    'testqnt',
    'testsant',]

def SMS_Mas(tel='',msg='',lms='false',fls='false',pmu='true'):

        # credentials Vicidial
        connM = {
            'user' : 'Api_UGYHS',
            'psw' : 'MP2JBEKOUY',
            'url' : 'https://sms.masivapp.com/SmsHandlers/sendhandler.ashx'}
        
        args = {'action': 'sendmessage',
                'username' : connM.get('user'),
                'password' : connM.get('psw'),
                'recipient' : '57'+tel,
                'messagedata' : msg,
                'longMessage' : lms,
                'flash' : fls,
                'premium' : pmu}
        
        b = requests.get(connM.get('url').replace('\n','')
                        ,params=args).text
        
        b = [jxmlease.parse(b)['response']['action'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['statuscode'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['statusmessage'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['messageid'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['recipient'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['messagetype'].get_cdata(),
        jxmlease.parse(b)['response']['data']['acceptreport']['messagedata'].get_cdata()]

        return b

def AL_Vici(list_id,campaign,active,descr,list_name,local_call_time,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+str(numip),
        'agc' : 'vicidial',
        'user' : 'soporte',
        'psw' : 'Bogota1234',
        'url' : 'http://{0}/{1}/non_agent_api.php?source=test&function=add_list&user={2}&pass={3}&list_id={4}&list_name={8}&campaign_id={5}&active={6}&list_description={7}&local_call_time={9}'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+str(numip),
        'agc' : 'vicidial',
        'user' : 'secetina',
        'psw' : '1233692646',
        'url' : 'http://{0}/{1}/non_agent_api.php?source=test&function=add_list&user={2}&pass={3}&list_id={4}&list_name={8}&campaign_id={5}&active={6}&list_description={7}&local_call_time={9}'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/AL_URL.txt","r") as f1:
        # al_url = f1.read()
        
    b = pd.DataFrame([requests.get(connV.get('url').format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    list_id,
                                    campaign,
                                    active,
                                    descr,
                                    list_name,
                                    local_call_time).replace('\n','')).text.split('|')])
    return b

def ALe_Vici(phone,list_id,Vendor_lead,numip):

    if int(numip) > 200:
        # n = '150'
        connV = {
        'server' : '10.150.1.'+numip,
        'agc' : 'vicidial',
        'user' : 'soporte',
        'psw' : 'Bogota1234',
        'url' : 'http://{0}/{1}/non_agent_api.php?source=test&user={2}&pass={3}&function=add_lead&phone_number=9{4}&list_id={5}&vendor_lead_code={6}'}
    else:
        # n = '152'
        connV = {
        'server' : '10.152.1.'+numip,
        'agc' : 'vicidial',
        'user' : 'secetina',
        'psw' : '1233692646',
        'url' : 'http://{0}/{1}/non_agent_api.php?source=test&user={2}&pass={3}&function=add_lead&phone_number=9{4}&list_id={5}&vendor_lead_code={6}'}

    # url
    # with open("/home/manuel/Documentos/WiseR/Vicidial/Templates/ALe_URL.txt","r") as f1:
        # ale_url = f1.read()
        
    b = pd.DataFrame([requests.get(connV.get('url').format(connV.get('server'),
                                    connV.get('agc'),
                                    connV.get('user'),
                                    connV.get('psw'),
                                    phone,
                                    list_id,
                                    Vendor_lead).replace('\n','')).text.split('|')])
    return b

# Tipificaciones
@method_decorator(csrf_exempt,name='dispatch')
class FileTipi(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # file_serializer.save()
            
            file_obj = request.data['file']
            data1 = get_data(file_obj)
            col = list(data1.keys())
            data = pd.DataFrame(data1[col[0]][1:],columns=data1[col[0]][0])
            try:
                data2 = pd.DataFrame(data1[col[1]][1:],columns=data1[col[1]][0])
            except:
                pass
            # print(data1[col[1]][2])

            cols = ['codigo1',
                    'codigo2',
                    'codigo3',
                    'codigo4',
                    'codigo5',
                    'codigo6',
                    'codigo7',
                    'codigo8',
                    'codigo9',
                    'codigo10',
                    'prioridad',
                    'indicador']

            #credenciales PostgreSQL produccion
            connP_P = {
                'host' : '10.150.1.77',
                'port' : '5432',
                'user':'bi',
                'password':'juanitoMeToco2020',
                'database' : 'login'}

            query = """select id,indicador
                    from public.indicadores_general
                    order by indicador ;"""
            
            # tipificaciones

            tipi = pd.DataFrame(columns=cols)
            tipi_n = pd.DataFrame(columns=cols)
            unq = pd.DataFrame()
            names = []
            n = 0


            for i in data:
                if data[i].dtype == 'object':
                    
                    names.append(i.lower())
                    tipi[i.lower()] = data[i].str.upper().str.strip()
                    unq = pd.concat([unq,
                                    data[i].str.upper().str.strip().drop_duplicates()\
                                        .reset_index(drop=True)],
                                    ignore_index=True,
                                    axis=1)
                    unq.columns = names
                    if i.lower().find('codigo') > -1:
                        
                        names.append(i.lower()+'_n')
                        unq = pd.concat([unq,pd.DataFrame(range(len(data[i].str.upper().str.strip()\
                                    .drop_duplicates().reset_index(drop=True))))],
                                    ignore_index=True,
                                    axis=1)
                        unq.columns = names
                        if i.lower()[-1] != '0':
                            unq[i.lower()+'_n'] = unq[i.lower()+'_n'] + (int(i.lower()[-1])*100)
                        else:
                            unq[i.lower()+'_n'] = unq[i.lower()+'_n'] + (int(i.lower()[-2:])*100)
                elif data[i].dtype == 'int64':
                    tipi[i.lower()] = data[i]
                    
            tipi.fillna(0,inplace=True)


            for i in unq:
                if i.lower().find('codigo') > -1 and i.lower().find('_n') == -1 and n == 0:
                    tipi_n[i] = pd.merge(tipi[[i]],
                                    unq[[i,i+'_n']],
                                    on = [i],
                                    how = "left",
                                    indicator = False)[i+'_n'].astype(int)
                    n += 1
                elif i.lower().find('codigo') > -1 and i.lower().find('_n') == -1:
                    tipi_n[[i]] = pd.merge(tipi[[i]],
                                                unq[[i,i+'_n']],
                                                on = [i],
                                                how = "left",
                                                indicator = False)[i+'_n'].astype(int)
            
            tipi_n['indicador'] = pd.merge(tipi['indicador'],
                                pd.read_sql(query,psycopg2.connect(**connP_P)),
                                on = ['indicador'],
                                how='left',
                                indicator = False)['id']
                        
            for i in tipi:
                if tipi[i].dtype == 'int64':
                    tipi_n[i] = tipi[i]

            for i in range(len(tipi_n)):
                Tipificaciones.objects.using(request.data.get('remark')).create(codigo01=tipi_n.loc[i,['codigo1']],
                                                                codigo02=tipi_n.loc[i,['codigo2']],
                                                                codigo03=tipi_n.loc[i,['codigo3']],
                                                                codigo04=tipi_n.loc[i,['codigo4']],
                                                                codigo05=tipi_n.loc[i,['codigo5']],
                                                                codigo06=tipi_n.loc[i,['codigo6']],
                                                                codigo07=tipi_n.loc[i,['codigo7']],
                                                                codigo08=tipi_n.loc[i,['codigo8']],
                                                                codigo09=tipi_n.loc[i,['codigo9']],
                                                                codigo10=tipi_n.loc[i,['codigo10']],
                                                                prioridad=tipi_n.loc[i,['prioridad']],
                                                                indicador=tipi_n.loc[i,['indicador']])

            for i in cols:
                if i.lower().find('codigo') > -1 and i in unq.columns:
                    for j in range(len(unq[[i,i+'_n']].dropna())):
                        Codigos.objects.using(request.data.get('remark')).create(descripcion=unq.loc[j,[i]][0],
                                                                codigo=unq.loc[j,[i+'_n']][0])
            
            if 'data2' in locals():
                for i in range(len(data2)):
                    NombreRama.objects.using(request.data.get('remark')).create(id=i+1,
                                                                nombre=data2.loc[i,['nombre cliente']][0])

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# envio SMS
class FileSMS(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, unidad, tipi):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # file_serializer.save()

            file_obj = request.data['file']
            data = get_data(file_obj)
            col = list(data.keys())
            data = pd.DataFrame(data[col[0]][1:],columns=data[col[0]][0])

            tarea = Tareas.objects.using(request.data.get('remark')).create(unidad_id = unidad,
                                                            registros = len(data),
                                                            clientes = len(data.cedula.drop_duplicates()),
                                                            obligaciones=0)
            asignacion = Asignaciones.objects.using(request.data.get('remark')).get(estado = True,
                                                                        unidad = unidad)
            
            for i in range(len(data)):
                Gestiones.objects.using(request.data.get('remark')).create(tarea_id = tarea.tarea_id
                ,usuario_id = 'SMS_BACK'
                ,deudor_id = data['cedula'][i]
                ,asignacion_id = asignacion.asignacion_id
                ,telefono = data['telefono'][i]
                ,canal = 'SMS'
                ,id_tipificacion = tipi
                ,descripcion = data['mensaje'][i])
            # print(data)
            
            for i in range(len(data)):
                SMS_Mas(str(data['telefono'][i]),
                            data['mensaje'][i])

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# consulta gestiones historicas
class ConsultaGestion(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Gestiones.objects.using(self.kwargs['db'])\
            .filter(deudor_id=self.kwargs['deudor_id'])
        return queryset
    serializer_class = GestionSerializer

# envio SMS
class FileCreacionTarea(APIView):

    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, numip, unidad, campaign, name):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            # file_serializer.save()

            file_obj = request.data['file']
            data = get_data(file_obj)
            col = list(data.keys())
            data = pd.DataFrame(data[col[0]][1:],columns=data[col[0]][0])

            tarea = Tareas.objects.using(request.data.get('remark')).create(unidad_id = unidad,
                                                            registros = len(data),
                                                            clientes = len(data.cedula.drop_duplicates()),
                                                            obligaciones=0)
            if int(numip) > 200:
                #credenciales MySQL
                connM = {
                    'host' : '10.150.1.'+str(numip),
                    'user':'desarrollo',
                    'password':'soportE*8994',
                    'database' : 'asterisk'}
            else:
                #credenciales MySQL
                connM = {
                    'host' : '10.152.1.'+str(numip),
                    'user':'desarrollo',
                    'password':'soportE*8994',
                    'database' : 'asterisk'}
            query = """
            select max(list_id)
            from asterisk.vicidial_lists vl
            order by campaign_id desc;
            """

            list_id = pd.read_sql(query,mysql.connector.connect(**connM))
            
            a = AL_Vici(str(list_id.iloc[0,0]+1),
                        campaign.replace(r'\n',''),
                        'Y',#active,
                        '--BLANK--',#descr,
                        name,#list_name,
                        '24hours',#local_call_time,
                        str(numip))
            
            # print(list_id.iloc[0,0]+1,campaign,name,str(numip))
            # print(a)

            if a.iloc[0,0].find('SUCCESS: add_list LIST HAS BEEN ADDED') > -1:
                # print(a)
                pass
                # return Response({'result' : a.iloc[0,0]},status = status.HTTP_201_CREATED)
            else:
                # print(a)
                return Response({'result' : a.iloc[0,0]},status = status.HTTP_400_BAD_REQUEST)

            for i in range(len(data)):
                a = ALe_Vici(data['telefono'][i],
                        list_id.iloc[0,0]+1,
                        data['cedula'][i],
                        str(numip))
                if a.iloc[0,0].find('SUCCESS: add_lead LEAD HAS BEEN ADDED') > -1:
                    # print(a)
                    pass
                else:
                    # print(a)
                    return Response({'result' : a.iloc[0,0]},status = status.HTTP_400_BAD_REQUEST)

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)