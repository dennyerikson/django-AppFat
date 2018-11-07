from django.conf.urls import url, include
from . import views
import appfat

urlpatterns = [
    # url( '', home),
    # url('register/', register, name='register')


    url(r'^$', views.home, name='home'),
    url('boleto/', views.boleto, name='boleto'),
    url('curso/', views.curso, name='curso'),
    url('sala/', views.sala, name='sala'),
    url('conecta/',views.conecta, name='conecta'),
    url('convenio/', views.convenio, name='convenio'),
    url('info/', views.info, name='info'),
    url('tutoriais/', views.tutoriais, name='tutoriais'),


]