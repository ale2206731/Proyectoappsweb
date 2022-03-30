from ast import If
from urllib import request
from django.shortcuts import render
from .models import  Comentario, Noticias
from .forms import ComentarioForm

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def about(request):
    return render(request, 'app/about-us.html')

def services(request):
    return render(request, 'app/services.html')

def tabsaccordions(request):
    return render(request, 'app/tabs-and-accordions.html')

def news(request):
    noticia = Noticias.objects.all()
   
    datos = {
       
        "Noticias" : noticia,
        
    }
    return render(request, 'app/news.html', datos)

def contact(request):
    datos = { 
        'comentarios' : Comentario,
        'form': ComentarioForm
    }
    if request.method == 'POST':
        formulario = ComentarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            datos['form'] = formulario
    return render(request, 'app/contact-us.html', datos)

def newspost(request):
    return render(request, 'app/news-post.html')

def Adecco1(request):
    return render(request, 'app/Adecco Industrial & Logistics.html')

def Terminos(request):
    return render(request, 'app/terms-and-conditions.html')


def Privacidad(request):
    return render(request, 'app/privacy-policy.html')

def Adecco2(request):
    return render(request, 'app/adecco2.html')

def Adecco3(request):
    return render(request, 'app/adecco3.html')

def Adecco4(request):
    return render(request, 'app/adecco4.html')

def Adecco5(request):
    return render(request, 'app/adecco5.html')

def Adecco6(request):
    return render(request, 'app/adecco6.html')

def Busqueda(request):
    if request.GET['Busqueda']:
        query=request.GET['Busqueda']
        noticias = Noticias.objects.filter(encabezado__icontains=query)
       
        datos= {
            "result" : noticias,
            "query" : query
        }
        return render(request, 'app/busquedas.html', datos)
    else:
        return render(request,'app/busquedas.html')