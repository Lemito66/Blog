from django import forms 
from .models import Post, Category

#choices = [('coding', 'Coding'), ('sports', 'Sports'), ('entertainment', 'Entertainment')]
choices = Category.objects.all().values_list('name', 'name')
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category','body')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la etiqueta'}),
            'author': forms.Select(attrs={'class': 'form-control',}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control', 'placeholder':'Categoría'}), # 'placeholder': 'Categoría, choices=choices,
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuerpo'}), 
        }
        
class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'category', 'body',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la etiqueta'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control',}), # 'placeholder': 'Categoría, choices=choices,
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Cuerpo'}), 
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }