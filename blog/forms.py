from django.forms import HiddenInput, IntegerField, ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "slug", "author", "body"]
