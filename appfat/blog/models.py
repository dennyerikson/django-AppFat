from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# consulta user
# class PostManager(models.Manager):
#     def search(self, query):
#         return self.get_queryset().filter(
#             models.Q(ra_icontains=query) | \
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

    dis_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    dis_cpf = models.CharField(max_length=11)
    dis_disciplina = models.CharField(max_length=300)
    dis_curso = models.CharField(max_length=300)
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
    status_status = models.TextField() 
    status_bolsa = models.TextField()
    status_ajuste = models.TextField()
    status_card = models.TextField()
    status_rematricula = models.TextField()
    status_boleto = models.TextField()
       
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

