from django.contrib.auth import forms
from .models import User

# Além do usuário personalizado, também criamos formulário personalizados
# Novamente, a única diferença entre as nossas classes e as originais do Django são o modelo referenciado, aqui indicamos o nosso model de Usuário (que possue bio)
# Assim como em User, criamos nossas próprias classes de form para que possamos ter liberdade de incrementalas com features novas, caso necessário
# Por enquanto elas ainda funcionam exatamente iguais à suas classes pais


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
