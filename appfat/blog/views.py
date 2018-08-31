# -*-coding: utf-8 -*-";
from django.utils import timezone
import csv
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from .forms import SatsForm, SimpleForm
from django.shortcuts import render, get_object_or_404


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
    
    status = Status.objects.filter(status_cpf=request.user) #tabela atenção

    sats, created = Sats.objects.get_or_create(sats_cpf=request.user, defaults={
        'sats_cpf':request.user, 'sats_check':'0','sats_quest_01':'0'
    })

    valor_rb = request.POST.get('rb_type')
    # post = get_object_or_404(Profile, pk=sats.id)
    # if request.method == "POST":        
    #     form = SatsForm(request.POST, instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    # else:    
    #     form = SatsForm(instance=sats)
   

    # form = SimpleForm()

    context = {'aluno':aluno, 'status':status, 'sats':sats, 'valor_rb': valor_rb}

    return render(request, 'blog/home.html', context)

""" BOLETOS """
@login_required
def boleto(request):
    boleto = Boleto.objects.filter(bol_cpf=request.user)
    return render(request, 'blog/boleto.html', {'boleto':boleto})

""" CURSO """
@login_required
def curso(request):

    aluno = Aluno.objects.get(alu_cpf=request.user) #dados aluno
    curso = Curso.objects.filter(cur_nome=aluno.alu_curso)
    
    for c in curso:
        coord = c

    context = {'curso':curso, 'aluno':aluno, 'coord':coord}

    return render(request, 'blog/curso.html', context)

""" SALA """
@login_required
def sala(request):
    sala = Sala.objects.filter(sala_cpf=request.user)
    return render(request, 'blog/sala.html', {'sala':sala})

""" CONECTA """
@login_required
def conecta(request):
    aluno = Aluno.objects.get(alu_cpf=request.user) #dados aluno
    conecta = Conecta.objects.filter(con_curso=aluno.alu_curso)
    return render(request, 'blog/conecta.html', {'conecta':conecta})

""" CONVENIO """
@login_required
def convenio(request):
    convenio = Convenio.objects.filter()
    return render(request, 'blog/convenio.html', {'convenio':convenio})

""" INFORMAÇÃO """
@login_required
def info(request):
    info = Info.objects.filter() #tabela informação
    context = {'info':info}
    return render(request, 'blog/info.html', context)

""" TUTORIAIS """
@login_required
def tutoriais(request):    
    return render(request, 'blog/tutoriais.html', {})

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

# def sats(request):
#     sats = Sats.objects.filter(sats_cpf=request.user)
#     if(len(sats) <= 0):
#         if request.method == "POST":
#             display_type = request.POST.get("display_type", None)
#         if display_type in ["0","1","2","3","4","5","6","7","8","9","10"]:
#             sats.sats_cpf = request.user
#             sats.sats_check = "1"
#             sats.sats_quest_01 = display_type
#             sats.created_date = timezone.now()
#             sats.save()
#     return render(request, 'blog/home.html', {'sats':sats})

    
    
            
