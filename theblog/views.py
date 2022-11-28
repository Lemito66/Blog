from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# Create your views here.
""" def home(request):
    return render(request, 'home.html') """
    
class HomeView(ListView):
    '''
        Crea una vista para visualizar
    '''
    model = Post
    template_name = 'home.html'
    
class ArticleDetailView(DetailView):
    '''
        Crea una vista para ver los detalles del post
    '''
    model = Post
    template_name = 'article_details.html'
    
class AddPostView(CreateView):
    '''
        Crea una vista para crear una vista
    '''
    model = Post
    template_name = 'add_post.html'
    fields = '__all__' # Todos los campos
    #fields = ('title', 'body') # Solo los campos que queremos