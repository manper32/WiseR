from django.urls import path
from Vicidial import  views
# from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('dial/<str:AgentUser>/<str:Phone>/<str:numip>/<str:VendorId>', views.Dial.as_view(), name='Dial'),
    path('hangup/<str:user>/<str:numip>', views.HangUp.as_view(), name='HangUp'),
    path('pause/<str:user>/<str:value>/<str:numip>', views.Pause.as_view(), name='Pause'),
    path('status/<str:user>/<str:status>/<str:numip>', views.Status.as_view(), name='Status'),
    path('pause_code/<str:user>/<str:value>/<str:numip>', views.PauseCode.as_view(), name='PauseCode'),
    path('HangUpManual/<str:user>/<str:value>/<str:status>/<str:numip>', views.HangUpManual.as_view(), name='HangUpManual'),
    path('ChangeIngroups/<str:user>/<str:numip>', views.ChangeIngroups.as_view(), name='ChangeIngroups'),
]