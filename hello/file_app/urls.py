from django.urls import path
from file_app import  views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('upload_task/<int:unidad>/<int:numip>/<str:name>/<str:campaign>/<int:callf>', views.FileCreacionTarea.as_view(), name='file_task'),
    path('upload_SMS/<int:unidad>', views.FileSMS.as_view(), name='file_SMS'),
    path('upload_tipi/<int:unidad>', views.FileTipi.as_view(), name='file_tipi'),
    # path('upload/', views.FileView.as_view(), name='file'),
    path('get_manage/<str:db>/<str:deudor_id>', views.ConsultaGestion.as_view(), name='consulta_Gestion'),
    path('get_call/<str:db>/<str:numip>', views.ConsultaTareaCall.as_view(), name='consulta_Call'),
    path('get_SMS/<str:db>', views.ConsultaTareaSMS.as_view(), name='consulta_SMS'),
    path('pause/', views.ConsultaVicidialPause.as_view(), name='VicidialPause'),
    path('CallReturn/<int:unidad>', views.RetornoLlamadas.as_view(), name='RetornoLlamdas'),
    path('upload_email/<int:unidad>', views.FileEmail.as_view(), name='file_email'),
    path('get_EMAIL/<str:db>', views.ConsultaTareaEMAIL.as_view(), name='consulta_Email'),
    path('upload_gescall/<int:unidad>', views.FileGesCall.as_view(), name='file_gescall'),
    path('get_GESCALL/<str:db>', views.ConsultaTareaGesCall.as_view(), name='consulta_gescall'),
    path('get_CampaignList/<str:db>', views.ConsultaCampaignList.as_view(), name='consultaCampaignList'),
    path('get_WolkRepChat/<int:num>', views.WolkvoxRepChat.as_view(), name='WolkvoxRepChat'),
    path('get_RETURN/<str:db>/<int:unidad>', views.ConsultaTareasReturn.as_view(), name='ConsultaReturn'),
    path('Excel_RETURN/<str:db>/<int:unidad>', views.ExcelTareasReturn.as_view(), name='ConsultaReturn'),
    path('get_shipment/<str:db>/<str:tipo>', views.ConsultaTareasSum.as_view(), name='ConsultaReturn'),
    path('HabeasData/<str:db>', views.CrearHabeasData.as_view(), name='HabeasData'),
    path('ExcelHabeasData/<str:db>/<str:li>/<str:ls>', views.ConsultaHabeasData.as_view(), name='ExcelHabeasData'),
    path('AuxIndicativos/', views.ConsultaAuxIndicativos.as_view(), name='AuxIndicativos'),
]