# -*-coding: utf-8 -*-";
import csv
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Aluno, Status, Info
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User


# def user(request):
#     user = request.user
#     return user

# consulta = user()

# metodo para passar dados confiltro para a home
# @login_required
# def home(request):
#     # filtro para consulta 
#     post = Post.objects.filter(dis_cpf=request.user) # informativos curso
#     aluno = Aluno.objects.filter(alu_cpf=request.user) #dados aluno
#     # curso = Post.objects.filter(dis_disciplina = post.dis_disciplina) #dados aluno
#     status = Status.objects.filter(status_cpf=request.user) #tabela atenção
#     info = Info.objects.filter() #tabela informação

#     #get context dos atributos de .models
#     context = {'aluno': aluno, 'status':status, 'info':info, 'post': post}

#     return render(request, 'blog.html', context)

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('accounts/')
#     else:
#         form = UserCreationForm()

#         args = {'form': form}
#         return render(request, 'registration/cadastro.html', args)
nome = []
@login_required
def home(request):
    aluno = Aluno.objects.filter(alu_cpf=request.user) #dados aluno
    # aluno = Aluno.alu_nome.filter(alu_cpf=request.user).only('alu_nome') #dados aluno
        
    # first_nome = str(aluno.alu_nome).split(' ')
    # return render(request, 'blog/home.html', {'aluno':aluno})
    return render(request, 'blog/home.html', {'aluno':aluno})

@login_required
def boleto(request):
    return render(request, 'blog/boleto.html', {})
@login_required
def curso(request):
    return render(request, 'blog/curso.html', {})
@login_required
def sala(request):
    return render(request, 'blog/sala.html', {})
@login_required
def conecta(request):
    return render(request, 'blog/conecta.html', {})
@login_required
def convenio(request):
    return render(request, 'blog/convenio.html', {})

@login_required
def info(request):
    info = Info.objects.filter() #tabela informação
    context = {'info':info}
    return render(request, 'blog/info.html', context)

# def login(request):
#     return render(request, 'login.html')

# def curso(request):
#     name_curso = Aluno.objects.filter(alu_curso=consulta).get()
#     return render(request, 'blog.html', {'curso':name_curso})

# def resgister(request):
#     template_name = 'registration/cadastro.html'
#     context = {
#         'form':UserCreationForm()
#     }
#     return render(request, 'registration/cadastro.html')

# """ carregar dados CSV """
# def cvs_list(request):
#     lista = []
#     dados_csv = csv.reader(open())
#     return render(request, {})
