from django.conf.urls import url
from .views import home, register

urlpatterns = [
    url( '', home),
    url('register/', register, name='register')
]