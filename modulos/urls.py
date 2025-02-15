from django.urls import path
from .views import *

urlpatterns =[
    path('api/get/', lista_modulos, name='lista'),
    path('registrar/', registrar_modulo, name='registrar'),
    path('json/', json_modulo, name='json'),
]