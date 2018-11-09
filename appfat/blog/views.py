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

    for a in aluno:
        conecta = a.alu_id_cur
      
    
    cur = Curso.objects.filter(cur_id_cur=conecta)
    for c in cur:
        id_uni = c.cur_id_uni
        # print(c.cur_nome)
    
    ############# Verificação da vaga conecta #############    
    cur_conecta = Conecta.objects.filter(con_id_cur=conecta)
    for c in cur_conecta:
        id_con = c.pk
        # print("curso", c.con_curso)

    try:
        if id_con > 0:
            conecta = 1        
    except:
        conecta = 0   
    # print("valor ", conecta) 
    ############## Verificação da vaga conecta #############

    sats, created = Sats.objects.get_or_create(sats_cpf=request.user, defaults={
        'sats_cpf':request.user, 'sats_check':'1','sats_quest_01':'0', 'created_date':timezone.now(),
    })
   
   ############# Cria status do user #############
    query, created = Status.objects.get_or_create(status_cpf=request.user, defaults={        
        'status_cpf':request.user, 
        'status_bolsa':"0",
        'status_ajuste':"0",
        'status_card':"0",
        'status_rematricula':"0",
        'status_boleto':"0",
        'created_date':timezone.now(),
        'published_date':timezone.now(),
        'status_author_id':1,
        'status_sala':"0",
        'status_status':"0"
    })
    ############# Cria status do user #############

    info_modal = InfoModal.objects.filter()
    
    # for m in info_modal:
    #     print(sats.sats_check, m.text10, m.title10, m.title9)
    """ get choices - persiste o valor do radiobutton """
    if request.method == "POST": 
        radio_form = SimpleForm(request.GET.get('ESCOLHA'))
        if radio_form.is_valid:                       
            valor_rb = request.POST.get('ESCOLHA')      
            # print('valor choice: {}'.format(valor_rb))
            try:
                sats.sats_check = '0'
                sats.sats_quest_01 = str(valor_rb)
                created_date = timezone.now(),
                sats.save() 
            except:
                sats, created = Sats.objects.get_or_create(sats_cpf=request.user, defaults={
                'sats_cpf':request.user, 'sats_check':'1','sats_quest_01':'0', 'created_date':timezone.now(),
    })
        
    else:
        radio_form = SimpleForm()
        # print('else')
    
    # post = get_object_or_404(Profile, pk=sats.id)
    # if request.method == "POST":        
    #     form = SatsForm(request.POST, instance=post)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    # else:    
    #     form = SatsForm(instance=sats)
   
    # print(type(int(sats.sats_check)),int(sats.sats_check), created)
    # sats_ = int(sats.sats_check)
    # if sats_ > 0:
    #     sats_ = 1
    # else:
    #     sats_ = 0
    # print("sats_", sats_)

    context = {'aluno':aluno, 'status':status, 'sats':sats, 'radio_form':radio_form,
    'info_modal':info_modal, 'conecta':conecta, 'id_uni':id_uni}

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
    curso = Curso.objects.filter(cur_id_cur=aluno.alu_id_cur)
    
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
    conecta = Conecta.objects.filter(con_id_cur=aluno.alu_id_cur)
    return render(request, 'blog/conecta.html', {'conecta':conecta})

""" CONVENIO """
@login_required
def convenio(request):
    aluno = Aluno.objects.get(alu_cpf=request.user) #dados aluno
    # provas = Provas.objects.filter(pro_curso='4')
    provas = Provas.objects.filter(pro_curso=aluno.alu_id_cur)
    return render(request, 'blog/convenio.html', {'provas':provas})

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


def ConsultasStaus():   
    b = Boleto.objects.get(bol_cpf=request.user)
    if(b.id > 0):
        status = '1'
    else:
        status = '0'
    
    return status



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

    
    
            
