from django.db import models

# Create your models here.
class relatorios(models.Model):
    nome_relatorio = models.CharField(max_length=100, blank=False, null= False, verbose_name='Nome do relatório')
    desc_relatorio = models.CharField(max_length=255, blank=True, null=True, verbose_name='Descrição do relatório')
    link_relatorio = models.URLField(blank=False, null=False, verbose_name='Url do relatório')
    img_relatorio = models.ImageField(upload_to='media_relatorio', blank=True, null=True, verbose_name='Foto')
    filial_relatorio = models.CharField(max_length=100, blank=False, null= False, verbose_name='Filial Relatório')
   
    def __str__(self):
        return f"{self.nome_relatorio}"
    


