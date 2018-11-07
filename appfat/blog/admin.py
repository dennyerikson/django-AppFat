from django.contrib import admin
from models import *

#adcionado os models para admin
admin.site.register(Post)
admin.site.register(Aluno)
admin.site.register(Status)
admin.site.register(Curso)
admin.site.register(InfoModal)
admin.site.register(Info)
admin.site.register(Sats)

