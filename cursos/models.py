from django.db import models

class Base(models.Model):
    criado = models.DateField('criacao', auto_now_add=True)
    atualizado = models.DateField('atualizacao', auto_now=True)
    ativo = models.BooleanField('ativo', default=True)

    class Meta:
        abstract = True


class Curso(Base):
    titulo = models.CharField('Nome', max_length=255)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['id']

    def __str__(self):
        return self.titulo


class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name='avaliacoes', on_delete=models.CASCADE)
    nome = models.CharField('nome', max_length=255)
    email = models.EmailField()
    comentario = models.TextField(blank=True, default='')
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['email', 'curso']
        ordering = ['id']
    
    def __str__(self):
        return f'{self.curso} avaliou o curso {self.curso} com nota {self.avaliacao}'