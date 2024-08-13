from django.urls import path
from Api.views import *
app_name = 'api'



urlpatterns = [
    path('', home, name='home'),
    path('getsettings/', get_settings, name='get_settings'),
    path('getstate/', get_state, name='get_state'),
    path('sendmessage/', send_message, name='send_message'),
    path('sendfile/', send_file, name='send_file'),

]