from django.urls import path
from file_app import  views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('upload_task/<int:unidad>/<int:numip>/<str:name>/<str:campaign>', views.FileCreacionTarea.as_view(), name='file_task'),
    path('upload_SMS/<int:unidad>/<int:tipi>', views.FileSMS.as_view(), name='file_SMS'),
    path('upload_tipi/', views.FileTipi.as_view(), name='file_tipi'),
    # path('upload/', views.FileView.as_view(), name='file'),
    path('get_manage/<str:db>/<str:deudor_id>', views.ConsultaGestion.as_view(), name='consulta_Gestion'),
    path('get_call/<str:db>', views.ConsultaTareaCall.as_view(), name='consulta_Call'),
]