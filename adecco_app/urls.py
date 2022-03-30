from django.urls import path, include
from .views import about, index, about, services, tabsaccordions, news, contact, newspost, Adecco1, Terminos,Privacidad, Adecco2, Adecco3, Adecco4, Adecco5, Adecco6, Busqueda
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', index, name='Inicio'),
    path('about/', about, name='Sobre Nosotros'),
    path('services/', services, name='Servicios'),
    path('tabsaccordions/', tabsaccordions, name='Pestañas y Acordes'),
    path('news/', news, name='Noticias'),
    path('contact-us/', contact, name='Contactanos'),
    path('news-post/', newspost, name='Noticias Publicadas'),
    path('Adecco Industrial & Logistics/',Adecco1, name='Adecco1'),
    path('terms-conditions/', Terminos, name='Terminos'),
    path('privacy-policy/', Privacidad, name='Privacidad'),
    path('AdeccoOffice/', Adecco2, name='Adecco2'),
    path('AdeccoMarketing/', Adecco3, name='Adecco3'),
    path('AdeccoExpert/', Adecco4, name='Adecco4'),
    path('AdeccoIT/', Adecco5, name='Adecco5'),
    path('AdeccoHealthcare/', Adecco6, name='Adecco6'),
    path('buscar/', Busqueda, name='buscar'),

]