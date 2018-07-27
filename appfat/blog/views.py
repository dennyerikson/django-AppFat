# -*-coding: utf-8 -*-";

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Aluno, Status, Info

# metodo para passar dados confiltro para a home
def home(request):
    # filtro para consulta 
    post = Post.objects.filter(dis_cpf='38019987894') # informativos curso
    aluno = Aluno.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #dados aluno
    status = Status.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #tabela atenção
    info = Info.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #tabela informação

    #get context dos atributos de .models
    context = {'aluno': aluno, 'status':status, 'info':info, 'post': post}

    return render(request, 'blog.html', context)

#add imageview in form
