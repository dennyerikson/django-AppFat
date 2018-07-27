from django.contrib import admin
from models import Post, Aluno, Info, Status

#adcionado os models para admin
admin.site.register(Post)
admin.site.register(Aluno)
admin.site.register(Status)
admin.site.register(Info)
