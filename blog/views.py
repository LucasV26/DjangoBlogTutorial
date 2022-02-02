from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import PostForm

# Aqui utilizamos views genéricas para agilizar a criação das nossas views básicas de listagem e detalhamento
# As views genéricas se baseiam no modelo MVT, ou seja, elas naturalmente irão requisitar um template HTML para retornar seus valores
# As views em Django são bem semelhantes aos COntrollers de SpringBoot e irão mapear as nossas rotas, recebendo requests e retornando responses
# Podemos estruturar as views em classes ou funções, próximo projeto -> estruturar views em funções e fazer elas retornarem JSON (API REST)


class ListPostView(ListView):
    model = Post


class DetailPostView(DetailView):
    model = Post

def CreatePostView(request):
    if request.method == "POST":
        newPostForm = PostForm(request.POST)
        if newPostForm.is_valid():
            newPost = newPostForm.save()
            if newPost:
                return HttpResponseRedirect('/blog')
    else:
        newPostForm = PostForm()

    return render(request, "post_form.html", {"form": newPostForm})

