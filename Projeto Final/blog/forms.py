from django import forms
from blog.models import Comentario

class ComentarioForm(forms.ModelForm):    
    usuario = forms.CharField(
        label = "Nome do usuário:",
        required = True,
        max_length = 100,
        widget= forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    comentario = forms.CharField(
        label = "Comentário:",
        required = True,
        max_length = 500,
        widget= forms.TextInput(
            attrs={
                'class':'form-control mb-3' 
            }
        )
    )
    
    class Meta: 
        model = Comentario
        fields = ['usuario', 'comentario']