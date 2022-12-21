from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    '''
        Formulario para añadir mas campos al USERCREATIONFORM porque por defecto solo tiene 3 campos
    '''
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True,max_length=80, label="Primer nombre")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True,max_length=80, label="Apellido")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}),required=True,max_length=80, label='Correo electrónico')
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )
        
    def __init__(self, *args, **kwargs):
        '''
            Función para dar estilo a los campos del formulario
        '''
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        

