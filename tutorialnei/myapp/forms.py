
#Imports
from django import forms
from .models import Item

#Importar o user model do Django
from django.contrib.auth.models import User


#Vamos utilizar o ModelForm do Django para utilizar o modelo Item que criamos para o formulário.
#Não precisamos de especificar mais nada sem ser o modelo que vamos utilizar e os field que queremos
#Que aparecam no formulário ao utilizador.
class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('item_name', 'item_price')


#A ideia aqui é a mesma que a do Django Form em cima mas usando o modelo user default que o Django
#dispõe.
class SignUpForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password')
        #Apenas um detalhes visual para a password ficar escondida
        widgets = {'password': forms.PasswordInput()}


#Esta form é diferente das anteriores pois não tá associada a um model, assim, temos que
#definir o que queremos mostrar em cada campo e de que forma.
class LoginForm(forms.Form):
    username = forms.CharField()

    #Detalhe visual aqui para esconder a password.
    password = forms.CharField(widget=forms.PasswordInput())