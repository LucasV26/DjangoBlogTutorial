from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Models em Django se assemelham à Entitys em Spring Boot
# A classse models.Model tem sua dependência injetada para que seja registrada como um modelo no sistema
# O nosso modelo é composto pelos campos da tabela desejada


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    # Relacionamentos são feitos através do método ForeignKey, recebendo o modelo referenciado como primeiro parâmetro
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created",)

    # A função __str__ tem o self injetado em sua declaração e funciona para trocar o nome que representa cada instância deste modelo
    def __str__(self):
        return self.title

    # A função getDetailPath utiliza a função reverse() do django para gerar a url absoluta referente ao nosso app
    # Passamos o argumento slug para que ele incremente à url o valor de slug do nosso modelo
    def getDetailPath(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
