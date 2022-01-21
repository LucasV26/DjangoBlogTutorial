from distutils.errors import PreprocessError
from django.contrib import admin
from .models import Post

# A marcação admin.register inclui o modelo especificado na página de admin
# A classe PostAdmin tem o modelo admin.ModelAdmin injetado em sua declaração e configura algumas coisas na página de admin
# Com list_display adicionamos os campos que queremos exibir no resumo do modelo
# Com prepopulated_fields inidcamos os campos que são preenchidos automaticamente e como isso é feito


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
