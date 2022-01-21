from django.views.generic import ListView, DetailView
from .models import Post

# Aqui utilizamos views genéricas para agilizar a criação das nossas views básicas de listagem e detalhamento
# As views genéricas se baseiam no modelo MVT, ou seja, elas naturalmente irão requisitar um template HTML para retornar seus valores
# As views em Django são bem semelhantes aos COntrollers de SpringBoot e irão mapear as nossas rotas, recebendo requests e retornando responses
# Podemos estruturar as views em classes ou funções, próximo projeto -> estruturar views em funções e fazer elas retornarem JSON (API REST)


class ListPostView(ListView):
    model = Post


class DetailPostView(DetailView):
    model = Post
