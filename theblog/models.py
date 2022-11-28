from cProfile import label
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Título')
    title_tag = models.CharField(max_length = 255, verbose_name='Nombre de la etiqueta')
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='Autor')
    body = models.TextField(verbose_name = 'Cuerpo')
    
    def __str__(self):
        return f'{self.title} | {self.author}'
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #Le pasamos el id del post y lo reederigimos a la vista article-detail
        return reverse('home') #Rederigimos a la página de home
