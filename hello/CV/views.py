from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from pymongo import MongoClient
from datetime import datetime
from ClaroCV.settings import host
from ClaroCV.settings import user
from ClaroCV.settings import port
from ClaroCV.settings import name
from ClaroCV.settings import psw
from time import time
import pandas as pd
import numpy as np
import psycopg2

def to_horiz(anwr_P,name,_id):
    #vertical horizontal telefonos
    anwr_P1 = anwr_P.pivot(index=0,columns=1)
    anwr_P1[_id] = anwr_P1.index
    
    #nombre de telefonos
    col1 = []
    i=0
    for i in range(anwr_P1.shape[1]-1):
        col1.append(name+str(i+1))
    col1.append(_id)
    
    anwr_P1.columns = col1
    
    return anwr_P1

class CVClaro(APIView):
    def post(self, request, *args, **kwargs):
        # try:
        initial = time()
        #credenciales PostgreSQL
        connP = {
            'host' : host,
            'port' : port,
            'user':user,
            'password':psw,
            'database' : name}
        
        # with open("/home/manuel/Documentos/WiseR/CVClaro/hello/ClaroCV/CV/templates/ClaroCV.txt","r") as f1:
        #     query1 = f1.read()
        # with open("/home/manuel/Documentos/WiseR/CVClaro/hello/ClaroCV/CV/templates/Tel_Claro.txt","r") as f2:
        #     query2 = f2.read()
        # with open("/home/manuel/Documentos/WiseR/CVClaro/hello/ClaroCV/CV/templates/Cor_Claro.txt","r") as f3:
        #     query3 = f3.read()
        with open("./hello/CV/templates/ClaroCV.txt","r") as f1:
            query1 = f1.read()
        with open("./hello/CV/templates/Tel_Claro.txt","r") as f2:
            query2 = f2.read()
        with open("./hello/CV/templates/Cor_Claro.txt","r") as f3:
            query3 = f3.read()
        anwr = pd.read_sql(query1.format('cbpo_claro_wiser','16'),psycopg2.connect(**connP))
        anwr['cedula1'] = anwr['cedula'].str.replace(r"[^0-9]",'',regex=True)
        anwr['obligacion1'] = anwr['obligacion'].str.replace(r"[^0-9]",'',regex=True)
        anwr['valor_a_pagar'] = anwr['valor_a_pagar'].str.replace(r"[^0-9]",'',regex=True)
        tipo= anwr.groupby(by=['cedula']
                        ,as_index=True).count()[['row_number']]
        tipo['tipo_cliente'] = np.where(tipo[['row_number']] > 1,
                                        'MULTI',
                                        'MONO')
        anwr = pd.merge(anwr,
                    tipo,
                    left_on=['cedula1'],
                    right_on=['cedula'],
                    how = 'left',
                    indicator = False).drop(['row_number_y'], axis=1)

        anwr['saldo_pendiente'] = anwr['valor_pago'].fillna(0) - anwr['valor_a_pagar'].fillna(0).astype(int)

        today = datetime.today().strftime('01-%m-%Y')
        client = MongoClient(host)
        # client.list_database_names()
        db = client['cbpo_claro_wiser']
        # db.list_collection_names()
        col = db['asignaciones']
        base = pd.DataFrame(list(col.find({'FechadeAsignacion':{'$gte':today}})))
        a = base.groupby(by=['deudor_id','obligacion_id']
                            ,as_index=False
                            ).agg({
                            'CRMOrigen':'max',
                            'PotencialMark':'max',
                            'PrePotencialMark':'max',
                            'WriteOffMark':'max',
                            'EdaddeDeuda':'max',#dias_mora
                            'NombreCampaa':'max',#segmento_bpo ---- no esta igual
                            # rango_bpo null en el comovamos
                            # tipo null en el comovamos
                            'FechadeVencimiento':'max',
                            'MIN':'max',#mincliente
                            # 'ValorScoring':'max',# valorscoring no llego en el ultimo
                            'NumeroReferenciadePago':'max',
                            'Montoinicial':'max',#monto_inicial
                            'ModInitCta':'max',#monto_ini_cuenta
                            'DeudaRealCuenta':'max',#deuda_real
                            'Segmento_BPO':'max',#segmentobpo
                            })
                
        a['deudor_id'] = a['deudor_id'].str.replace(r"[^0-9]",'',regex=True)
        a['obligacion_id'] = a['obligacion_id'].str.replace(r"[^0-9]",'',regex=True)
        cv = pd.merge(anwr,a,
                    left_on=['cedula1','obligacion1'],
                    right_on=['deudor_id','obligacion_id'],
                    how = 'left',
                    indicator = False).drop(['deudor_id','obligacion_id','cedula1','obligacion1']
                                            , axis=1)

        cv['descuento'] = '%'+cv['descuento'].fillna(0).astype(int).astype(str)
        for i in ['Montoinicial','ModInitCta','DeudaRealCuenta','saldo_pendiente',
                'valor_descuento','valor_pago','valor_a_pagar']:
            cv[i] = '$'+cv[i].astype(float).round().fillna(0).astype(int).astype(str)

        cv.columns = [
            'row_number',
            'deudor_id',#'cedula',
            'obligacion_id',#'obligacion',
            'unico',#'unico',
            'nombredelcliente',#'nombre',#nombredelcliente
            'ind_m4',# 'perfil_mes_4',
            'ind_m3',# 'perfil_mes_3',
            'ind_m2',# 'perfil_mes_2',
            'ind_m1',# 'perfil_mes_1',
            'fecha_primer_gestion',# 'primer_gestion',
            'fecha_ultima_gestion',# 'ultima_gestion',
            'fec_ultima_marcacion',# 'ultimo_alo',
            'indicador',#'estado_contacto',???
            'indicador',#'mejor_gestion_mes_actual',
            'asesor',# 'nombre_asesor_mejor_gestion',
            'fecha_gestion',#'fecha_mejor_gestion',
            'phone',# 'telefono_mejor_gestion',
            'indicador_hoy',#'mejor_gestion_hoy',
            'usuario_mejor_gestion_hoy',
            'llamadas',# 'cantidad_llamadas',
            'sms',# 'cantidad_sms',
            'correos',#'cantidad_email',
            'whatsapp',# 'cantidad_whatsapp',
            'visitas',# 'cantidad_visitas',
            'gescall',# 'cantidad_gescall',
            'agente_virtual',# 'cantidad_agente_virtual',-----------se incluye????
            'total_gestiones',# 'total_gestiones',
            'cantidad_contacto',#--------------------------------se incluye??
            'no_contacto',# 'cantidad_no_contacto',
            'valor_compromiso',#'valor_compromiso',
            'fecha_pago_compromiso',# 'fecha_compromiso',
            'nombre_usuario_compromiso',#------------------------se incluye??
            'estado_acuerdo',# 'estado_acuerdo',
            'valor_pago',# 'valor_pago',
            'fecha_pago',# 'fecha_pago',
            'telefono_positivo',# 'telefono_positivo',
            'fecha_telefono_positivo',
            'cantidad_telefono_positivo',
            'fecha_compromiso',
            'porcentaje_descuento',#'descuento',
            'valor_descuento',#'valor_descuento',
            'valor_a_pagar',#'valor_pago',
            'estado',#estado
            'tipo_cliente',
            'saldo_pendiente',
            'crmorigen',# 'CRMOrigen',
            'potencialmark',# 'PotencialMark',
            'prepotencialmark',# 'PrePotencialMark',
            'writeoffmark',# 'WriteOffMark',
            'dias_mora',# 'EdaddeDeuda',
            'NombreCampaa',#xxxxxxxxxxxxxxxxxxxxx--------------------------
            'fechadevencimiento',# 'FechadeVencimiento',
            'mincliente',#'MIN',
            'numeroreferenciadepago',#'NumeroReferenciadePago',
            'monto_inicial',# 'Montoinicial',
            'monto_ini_cuenta',#'ModInitCta',
            'deuda_real',#'DeudaRealCuenta'
            'segmento_bpo']

        order = ['deudor_id'
        ,'obligacion_id'
        ,'nombredelcliente'
        ,'estado'
        ,'tipo_cliente'
        ,'unico'
        ,'crmorigen'
        ,'potencialmark'
        ,'prepotencialmark'
        ,'writeoffmark'
        ,'dias_mora'
        ,'segmento_bpo'
        # rango_bpo--        noooooo
        # tipo--             noooooo
        ,'fechadevencimiento'
        ,'mincliente'
        # valorscoring
        ,'numeroreferenciadepago'
        ,'monto_inicial'
        ,'monto_ini_cuenta'
        ,'porcentaje_descuento'
        ,'valor_descuento'
        ,'valor_a_pagar'
        ,'deuda_real'
        ,'valor_pago'
        ,'saldo_pendiente'
        ,'fecha_pago'
        ,'fecha_compromiso'
        ,'fecha_pago_compromiso'
        ,'valor_compromiso'
        ,'estado_acuerdo'
        ,'ind_m4'
        ,'ind_m3'
        ,'ind_m2'
        ,'ind_m1'
        ,'fecha_primer_gestion'
        ,'fecha_ultima_gestion'
        ,'indicador'
        ,'phone'
        ,'asesor'
        ,'fecha_gestion'
        # contactabilidad
        ,'indicador_hoy'
        # repeticion--------calcular
        ,'llamadas'
        ,'sms'
        ,'correos'
        ,'gescall'
        ,'whatsapp'
        ,'visitas'
        ,'no_contacto'
        ,'total_gestiones'
        ,'telefono_positivo'
        ,'fec_ultima_marcacion']

        tel = pd.read_sql(query2,psycopg2.connect(**connP))
        cor = pd.read_sql(query3,psycopg2.connect(**connP))
        tel.columns = [0,1,2]
        anwr_P1 = to_horiz(tel,'phone','deudor_id')
        anwr_C1 = cor.drop_duplicates(subset=['deudor_id'])

        #renombrar campos correos
        anwr_C1.columns = ['deudor_id','mail0','mail1']

        cv = pd.merge(cv[order],anwr_P1,on = ["deudor_id"]\
                    ,how = "left",indicator = False)
        cv = pd.merge(cv,anwr_C1,on = ["deudor_id"]\
                    ,how = "left",indicator = False)

        # cv.to_csv('/home/manuel/Documentos/WiseR/CVClaro/hello/ClaroCV/CV/templates/ComoVamos/CV.csv',index=False,sep='|',encoding='utf-8-sig')
        cv.to_csv("./hello/CV/templates/ComoVamos/CV.csv",index=False,sep='|',encoding='utf-8-sig')
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"),'ClaroCV-end',time()-initial)
        return Response({'Time':time()-initial}, status=status.HTTP_201_CREATED)
        # except:
        #     return Response({'Result':'Error'}, status=status.HTTP_400_BAD_REQUEST)
