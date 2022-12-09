from cProfile import label
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.name}'
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #Le pasamos el id del post y lo reederigimos a la vista article-detail
        return reverse('home') #Rederigimos a la página de home
class Post(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Título')
    title_tag = models.CharField(max_length = 255, verbose_name='Nombre de la etiqueta')
    author = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name='Autor')
    body = models.TextField(verbose_name = 'Cuerpo')
    post_date = models.DateField(auto_now_add=True, verbose_name='Fecha de publicación')
    category = models.CharField(max_length = 255, verbose_name = 'Categoría', default='Sin categoría')
    
    def __str__(self):
        return f'{self.title} | {self.author}'
    
    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id))) #Le pasamos el id del post y lo reederigimos a la vista article-detail
        return reverse('home') #Rederigimos a la página de home
