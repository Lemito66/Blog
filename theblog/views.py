from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditPostForm, CategoryForm
from django.urls import reverse_lazy
# Create your views here.
""" def home(request):
    return render(request, 'home.html') """
    
class HomeView(ListView):
    '''
        Crea una vista para visualizar
    '''
    model = Post
    template_name = 'home.html'
    #ordering = ['id']
    ordering = ['-post_date'] #Ultima publicación primero
    
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
    form_class = PostForm #Le pasamos el formulario que hemos creado
    template_name = 'add_post.html'
    #fields = '__all__' # Todos los campos
    #fields = ('title', 'body') # Solo los campos que queremos
    
class AddCategoryView(CreateView):
    '''
        Crea una vista para crear una vista
    '''
    model = Category
    form_class = CategoryForm #Le pasamos el formulario que hemos creado
    template_name = 'add_category.html'
    #fields = '__all__' # Todos los campos
    #fields = ('title', 'body') # Solo los campos que queremos
    
class UpdatePostView(UpdateView):
    '''
        Crea una vista para actualizar un post
    '''
    model = Post
    form_class = EditPostForm #Le pasamos el formulario que hemos creado
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']
    
class DeletePostView(DeleteView):
    '''
        Crea una vista para eliminar un post
    '''
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')