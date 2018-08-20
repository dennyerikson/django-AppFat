from django.conf.urls import url
from .views import home, boleto, curso, sala, conecta, convenio, Info

urlpatterns = [
    # url( '', home),
    # url('register/', register, name='register')


    url('', home),
    url('/boleto/', boleto),
    url('/curso/', curso),
    url('/sala/', sala),
    url('/conecta/', conecta),
    url('/convenio/', convenio),
    url('/info/', Info),

]