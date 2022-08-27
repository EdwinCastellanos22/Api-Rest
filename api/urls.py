from django.urls import path
from .views import Mivista


urlpatterns= [
    path('usuarios/', Mivista.as_view(), name='miVista'),
    path('usuarios/<int:id>', Mivista.as_view(), name='vistaSimple')

]