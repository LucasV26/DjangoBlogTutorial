from unicodedata import name
from django.urls import path
from . import views

# Configuramos app_name e o atributo name de path para não termos problemas com rotas semelhantes em apps diferentes
# path() conecta uma rota a uma view
#   Primeiro parametro -> rota ou variável da rota
#   Segundo paramentro -> view a ser carregada
#   Terceiro parametro -> explicado no primeiro comentário

# O parametro <slug:slug> indica que uma variável slug deve ser carregada e essa variável corresponde ao campo slug do nosso model

app_name = "blog"

urlpatterns = [
    path("", views.ListPostView.as_view(), name="list"),
    path("<slug:slug>/", views.DetailPostView.as_view(), name="detail"),
]
