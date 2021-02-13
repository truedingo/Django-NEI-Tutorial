from django.shortcuts import render, redirect

#1. ADICIONAR IMPORT
from django.views.generic import View

#Importar o nosso Modelo
from .models import Item

#Importar o user model do Django
from django.contrib.auth.models import User

#Importar o form
from .forms import ItemForm, SignUpForm, LoginForm

#Importar as funções built in do Django
from django.contrib.auth import authenticate, login, logout

#Método que encripta a pass
from django.contrib.auth.hashers import make_password

# Create your views here.

#2. CRIAR A CLASSE PRIMEIRA_VIEW

#Quando se usa a Class based Views, é necessário criar duas funções, get e post.
#GET e POST são métodos HTTP, estas funções vão ser automaticamente
#chamadas pelo Django de acordo com o que estamos a fazer.

#def get(self, request) -> Esta função vai ser chamada pelo Django
#sempre que se dá um método GET numa página web,
#em termos práticos, GETs são normalmente chamados quando entramos numa
#página e queremos ver o que esta contém, sem qualquer input
#do utilizador, no entanto, podem ter outras aplicações.

#def post(self,request) -> Esta função vai ser chamada pelo Django
#sempre que um método POST é chamado numa página web. Em termos práticos,
#POSTs são usados para obter dados. Exemplos como preencher
#um formulário de login e carregar no botão vão gerar POST requests.
class primeira_view(View):
    def get(self, request):
            
            #Vamos buscar a lista de todos os items existentes na BD.
            #Esta chamada retorna um QuerySet com a lista de items.
            item_list = Item.objects.all()


            print(item_list)

            #Vamos utilizar o render, esta função serve para renderizar os contéudos do
            #que estamos a fazer no nosso get na nossa página web. Esta recebe uma request e o ficheiro html
            #para a página que vamos mostrar.

            #Podemos também usar com o render um outro parâmetro, um dicionário. Este dicionário funciona
            #exatamente como dicionários em Python e podemos passar qualquer tipo de informação às nossas
            #páginas HTML utilizando este método. De modo a que os items sejam mostrados na página html
            #Precisamos de os "passar" à pagina HTML. Assim, passamos como último argumento um dicionário
            #que contém o nosso item_list com os resultados da nossa Query de todos os produtos na BD.
            print("Entrei no get")
            return render(request, 'pagina.html', {'item_list': item_list})

    def post(self, request):


        #Toda a informação das requests tá guardada em request.
        #Neste caso, queremos obter os dados referentes ao POST request que tivemos
        #Para isso, precisamos simplesmente do name do elemento HTML de que queremos
        #a informação.  O name que estabelecemos para o o input da pesquisa é
        #search_input.
        search_text = request.POST['search_input']
        print("search input: ", search_text)

        #O Django contém bastantes queries úteis. Para a pesquisa simplesmente
        #precisamos de filtrar por item_name e ver se este contém a palavra que recebemos.
        #Para isto usa-se filter([atributo_do_modelo]__iexact) que é um filtro case
        #insensitive para a pesquisa.
        item_list = Item.objects.filter(item_name__icontains=search_text)
        print(item_list)
        return render(request, 'pagina.html', {'item_list': item_list})


class add_product_view(View):
    def get(self, request):

        #O primeiro passo é inicializar o form. Depois, temos de o passar para o nosso HTML como fizemos com as
        #item_lists
        item_form = ItemForm()

        return render(request, 'addproduct.html', {'item_form': item_form})

    def post(self, request):

        #Agora, para obtermos a informação do formulário vamos simplesmente inicializar o form com a informação
        #do request POST
        item_form = ItemForm(request.POST)
        print("item_form details: ", item_form.data['item_name'], " ", item_form.data['item_price'])

        #Depois de termos o form populado, podemos facilmente adicionar o item à Base de Dados com .save()
        item_form.save()

        #Em vez de voltar a fazer render quando não há necessidade (não vamos mostrar
        #nada de novo), podemos simplesmente fazer redirect para
        #a nossa view add_product_view utilizando o name do URL que configuramos.
        return redirect('addprod')


class sign_up_view(View):
    def get(self, request):
        signup_form = SignUpForm();
        return render(request, 'signup.html', {'signup_form': signup_form})

    def post(self, request):
        signup_form = SignUpForm(request.POST)

        #É necessário validarmos o form para usar as funções built-in de login e authenticate do Django

        if signup_form.is_valid():
            #Temos que fazer umas mudanças para criar o utilizador, vamos ter de alterar
            #o campo da password porque o django não guarda palavras passe sem serem
            #encriptadas. commit=false significa que vamos criar o utilizador mas não
            #o guardar ainda enquanto não encriptarmos a palavra passe
            signup_form = signup_form.save(commit=False)

            #Guardar username e password antes de dar save do form pois este fica inválido após o save.
            username = signup_form.username
            
            #precisamos da palavra passe original para fazer o authenticate e login
            password = signup_form.password

            #Encriptar a palavra passe
            signup_form.password = make_password(password)

            #Guardar o utilizador
            signup_form.save()

            #Utilizar a função de autenticação do Django, segundo a documentação deve ser feito desta maneira
            user = authenticate(request, username=username, password=password)
            
            #Se o User foi autenticado
            if user is not None:
                #Usar a função built in de login do Django, que guarda os detalhes do user numa request
                #durante algum periodo de tempo ou até darmos logout
                login(request, user)
                #Após o login, vamos redirrecionar para a página principal
                return redirect('pagina')
            return redirect('signup')
        return redirect('signup')


def logout_view(request):
    logout(request)
    return redirect('pagina')






class login_view(View):
    def get(self, request):
        login_form = LoginForm()

        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():

            #Ir buscar username e password usando cleaned_data depois de validar o form
            #(é a única maneira de o fazer)
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina')
            else:
                return redirect('login')
        else:
            return redirect('login')
