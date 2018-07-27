# -*-coding: utf-8 -*-";

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Aluno, Status, Info

consulta = '38019987894'

# metodo para passar dados confiltro para a home
def home(request):
    # filtro para consulta 
    post = Post.objects.filter(dis_cpf=consulta) # informativos curso
    aluno = Aluno.objects.filter(alu_cpf=consulta) #dados aluno
    # curso = Post.objects.filter(dis_disciplina = post.dis_disciplina) #dados aluno
    status = Status.objects.filter(status_cpf=consulta) #tabela atenção
    info = Info.objects.filter() #tabela informação

    #get context dos atributos de .models
    context = {'aluno': aluno, 'status':status, 'info':info, 'post': post}

    return render(request, 'blog.html', context)

#add imageview in form
