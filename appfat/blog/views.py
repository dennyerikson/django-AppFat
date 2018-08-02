# -*-coding: utf-8 -*-";

from django.shortcuts import render
from django.utils import timezone
from .models import Post, Aluno, Status, Info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# def user(request):
#     user = request.user
#     return user

# consulta = user()

# metodo para passar dados confiltro para a home
@login_required
def home(request):
    # filtro para consulta 
    post = Post.objects.filter(dis_cpf=request.user) # informativos curso
    aluno = Aluno.objects.filter(alu_cpf=request.user) #dados aluno
    # curso = Post.objects.filter(dis_disciplina = post.dis_disciplina) #dados aluno
    status = Status.objects.filter(status_cpf=request.user) #tabela atenção
    info = Info.objects.filter() #tabela informação

    #get context dos atributos de .models
    context = {'aluno': aluno, 'status':status, 'info':info, 'post': post}

    return render(request, 'blog.html', context)


# def curso(request):
#     name_curso = Aluno.objects.filter(alu_curso=consulta).get()
#     return render(request, 'blog.html', {'curso':name_curso})

#add imageview in form
