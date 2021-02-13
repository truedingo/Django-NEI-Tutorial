from django.shortcuts import render

#1. ADICIONAR IMPORT
from django.views.generic import View

#Importar o nosso Modelo
from .models import Item

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
        print("Nada, por agora.")


class add_product_view(View):
    def get(self, request):
            return render(request, 'addproduct.html')

    def post(self, request):
        print("Nada, por agora.")


class login_view(View):
    def get(self, request):
            return render(request, 'login.html')

    def post(self, request):
        print("Nada, por agora.")


class sign_up_view(View):
    def get(self, request):
            return render(request, 'signup.html')

    def post(self, request):
        print("Nada, por agora.")
