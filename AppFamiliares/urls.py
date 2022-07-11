from django.urls import path
from .views import familiar2, familiar1, familiar3, inicio, Familiares, Negocios, Inmobiliarios, FamiliaresFormulario, NegociosFormulario, InmobiliariosFormulario

urlpatterns = [
    path('familiar1/',familiar1),
    path('familiar2/',familiar2),
    path('familiar3/',familiar3),
    path('', inicio, name='inicio'),
    path('Familiares/', Familiares, name='Familiares'),
    path('Negocios/', Negocios, name='Negocios'),
    path('Inmobiliarios/', Inmobiliarios, name='Inmobiliarios'),
    path('FamiliaresFormulario', FamiliaresFormulario, name= 'FamiliaresFormulario'),
    path('NegociosFormulario', NegociosFormulario, name= 'NegociosFormulario'),
    path('InmobiliariosFormulario', InmobiliariosFormulario, name= 'InmobiliariosFormulario'),

]