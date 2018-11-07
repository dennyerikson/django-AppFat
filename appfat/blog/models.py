from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# consulta user
# class PostManager(models.Manager):
#     def search(self, query):
#         return self.get_queryset().filter(
#             models.Q(ra_icontains=query) | \  # ou 
#             models.Q(author_icontains=query)
#         )


# dados modelo aluno
class Aluno(models.Model):
    alu_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    alu_cpf=models.CharField(max_length=11)
    alu_ra=models.CharField(max_length=20)
    alu_nome=models.CharField(max_length=200)
    alu_tel=models.CharField(max_length=30)
    alu_cel=models.CharField(max_length=30)
    alu_email=models.CharField(max_length=150)
    alu_curso=models.CharField(max_length=200) # add coluna do curso 
    alu_status=models.CharField(max_length=20)
    alu_id_cur=models.CharField(max_length=2)

    created_date = models.DateTimeField(
        default = timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.alu_cpf

# dados post aluno
class Post(models.Model):
    #removi coluna do curso
    dis_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dis_cpf = models.CharField(max_length=11)
    dis_disciplina = models.CharField(max_length=300)
    dis_status = models.CharField(max_length=100)
    dis_data = models.CharField(max_length=50)
    dis_sala = models.CharField(max_length=50)
    dis_bloco = models.CharField(max_length=50)
    
    
    created_date = models.DateTimeField(
        default = timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.dis_disciplina

# dados status aluno
class Status(models.Model):

    status_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status_cpf = models.CharField(max_length=11)
    status_status = models.CharField(max_length=2) 
    status_bolsa = models.CharField(max_length=2)
    status_ajuste = models.CharField(max_length=2)
    status_card = models.CharField(max_length=2)
    status_rematricula = models.CharField(max_length=2)
    status_boleto = models.CharField(max_length=2)
    status_sala = models.CharField(max_length=2)
       
    created_date = models.DateTimeField(
    default = timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.status_cpf

    # object PostManager()
  

# dados info aluno
class Info(models.Model):

    info_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    info_title = models.CharField(max_length=100)
    info_informacao = models.TextField() 
    
    created_date = models.DateTimeField(
    default = timezone.now)

    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.info_informacao

    # object PostManager()

class Sats(models.Model):
    sats_cpf = models.CharField(max_length=11)
    sats_check = models.CharField(max_length=2)
    sats_quest_01 = models.CharField(max_length=2)
    created_date = models.DateTimeField(
    default = timezone.now)
   
    def __str__(self):
        return self.sats_check

""" modelo radio button"""
GENDER_CHOICES = (
   ('rb1', '1'),
   ('rb2', '2'),
   ('rb3', '3'),
   ('rb4', '4'),
   ('rb5', '5'),
   ('rb6', '6'),
   ('rb7', '7'),
   ('rb8', '8'),
   ('rb9', '9'),
   ('rb10', '10'),
)
class Profile(models.Model):
    pro_cpf = models.CharField( max_length=11)
    pro_check = models.CharField( max_length=10)
    pro_gender = models.CharField(choices=GENDER_CHOICES, max_length=20)
""" modelo radio button"""

# model de boletos
class Boleto(models.Model):
    bol_cpf = models.CharField( max_length=11)
    boleto= models.CharField(max_length=150) #nome titulo
    data= models.CharField(max_length=30) #data titulo
    status= models.CharField(max_length=30) #status titulo
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.boleto

#model do curso
class Curso(models.Model):
    cur_nome = models.CharField(max_length=150)
    cur_status = models.CharField(max_length=150) 
    cur_prof = models.CharField(max_length=150)
    cur_contato = models.CharField(max_length=150)
    cur_nome_coor = models.CharField(max_length=150)
    cur_cont_coor= models.CharField(max_length=150)
    cur_id_cur=models.CharField(max_length=2)
    cur_id_uni=models.CharField(max_length=2)

    def __str__(self):
        return self.cur_nome

#sala especial
class Sala(models.Model):
    sala_cpf = models.CharField(max_length=11)
    sala_dis = models.TextField(max_length=300)
    sala_dados = models.TextField(max_length=150)
    sala_sala = models.TextField(max_length=30)

    def __str__(self):
        return self.sala_dis

#conecta
class Conecta(models.Model):
    con_vaga = models.TextField(max_length=300)
    con_id = models.TextField(max_length=30)
    con_curso = models.TextField(max_length=300)
    con_id_cur = models.CharField(max_length=2)

    def __str__(self):
        return self.con_vaga
    
#convenio e parcerias
class Convenio(models.Model):
    conv_title = models.TextField(max_length=100)
    conv_info = models.TextField(max_length=300)

    def __str__(self):
        return self.conv_title


class InfoModal(models.Model):
    text1 = models.CharField(max_length=130)
    text2 = models.CharField(max_length=130)
    text3 = models.CharField(max_length=130)
    text4 = models.CharField(max_length=130)
    text5 = models.CharField(max_length=130)
    text6 = models.CharField(max_length=130)
    text7 = models.CharField(max_length=130)
    text8 = models.CharField(max_length=130)
    text9 = models.CharField(max_length=130)
    text10 = models.CharField(max_length=130)# texto dedicado a pesquisa
    title1 = models.CharField(max_length=30)
    title2 = models.CharField(max_length=30)
    title3 = models.CharField(max_length=30)
    title4 = models.CharField(max_length=30)
    title5 = models.CharField(max_length=30)
    title6 = models.CharField(max_length=30)
    title7 = models.CharField(max_length=30)
    title8 = models.CharField(max_length=30)
    title9 = models.CharField(max_length=30)
    title10 = models.CharField(max_length=30)# Title dedicado a pesquisa
        