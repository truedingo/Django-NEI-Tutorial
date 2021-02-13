"""tutorialnei URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#1. ADICIONAR OS IMPORTS
from myapp import views
from django.conf.urls import url

#2. ALTERAR PARA O SEGUINTE
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    #Configurar o URL, aqui estamos a dizer que o URL definido como o regex '^$' vai ativar a função
    #primeira_views na nossa views.py. Não é preciso saber muito sobre regex, pensem apenas que
    #'^$' representa como configuramos a homepage. No caso em cima, o URL para aceder ao nosso admin
    #do Django quando escrevemos /admin no browser. name serve simplesmente para dar um nome ao URL o que
    #torna mais fácil chama-lo noutros sítios de for preciso.
    url(r'^$', views.primeira_view.as_view(), name='pagina'),
    url(r'^addprod', views.add_product_view.as_view(), name='addprod'),
    url(r'^login', views.login_view.as_view(), name='login'),
    url(r'^signup', views.sign_up_view.as_view(), name='signup'),
    url(r'^logout', views.logout_view, name='logout'),
]
