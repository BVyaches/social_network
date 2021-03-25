from django.contrib.auth.forms import forms
from .models import Post


class CreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {'text': 'Текст',
                  'group': 'Группа'
                  }
