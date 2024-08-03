from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=30)
    rg = models.CharField(null=False, blank=False, max_length=90)
    cpf = models.CharField(null=False, blank=False, max_length=30)
    data_nascimento = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    codigo_curso = models.CharField(null=False, blank=False, max_length=30)
    descricao = models.CharField(null=False, blank=False, max_length=100)
    nivel_option = [
        ('Basico', 'Basico'),
        ('Intermediario', 'Intermediario'),
        ('Avançado', 'Avançado'),
    ]
    nivel = models.CharField(null=False, blank=False, max_length=100, choices=nivel_option, default="Basico")

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    periodo_options = [
        ('Matutino', 'Matutino'),
        ('Vespertino', 'Vespertino'),
        ('Noturno', 'Noturno'),
    ]

    periodo = models.CharField(
        blank=False,
        null=False,
        choices=periodo_options,
        max_length=20,
        default='Matutino'
    )

    aluno = models.ForeignKey(
        to=Aluno,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    curso = models.ForeignKey(
        to=Curso,
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.aluno}, {self.curso}'
