from django.contrib.auth import admin as user_admin
from django.contrib import admin
from .models import User
from .forms import UserCreationForm, UserChangeForm

# É necessário que o seu usuário personalizado substitua o usuário padrão do Django, para isso, configuramos duas coisas
# A primeira pode ser encontrada no arquivo tutorialdjango.settings.py
# A segunda é a extensão da classe UserAdmin na nossa nova classe UserAdmin


@admin.register(User)
class UserAdmin(user_admin.UserAdmin):
    # Toda modificação feita nesta classe é baseada na classe mãe user_admin.UserAdmin
    # Para saber mais modificações possíveis, acessar esta classe
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = user_admin.UserAdmin.fieldsets + (
        ("Biografia", {'fields': ("bio",)}),
    )

    list_display = user_admin.UserAdmin.list_display + ("bio",)
