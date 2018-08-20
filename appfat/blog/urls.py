from django.conf.urls import url, include
import blog
from . import views

urlpatterns = [
    # url( '', home),
    # url('register/', register, name='register')


    url('', views.home, name='home'),
    url(r'^boleto/$', views.boleto, name='boleto'),
    url('curso/', views.curso, name='curso'),
    url('sala/', views.sala, name='sala'),
    url('conecta/',views.conecta, name='conecta'),
    url('convenio/', views.convenio, name='convenio'),
    url('info/', views.Info, name='info'),


]