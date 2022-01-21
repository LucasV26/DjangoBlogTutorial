from django.db import models
from django.contrib.auth.models import AbstractUser

# É interessante a criação de um modelo próprio de usuário para que você tenha controle e possa atualizá-lo conforme as necessidades do projeto
# Inicialmente o seu Usuário vai ser uma pura extensão do AbstractUser do Django (que já existe e já é bem completo), mas ao criar seu próprio modelo, você fica no controle das possiveis mudanças
# Aqui, por exemplo, adicionamos o campo bio para que nosso usuário personalizado possua uma biografia


class User(AbstractUser):
    bio = models.TextField(blank=True)
