from django.forms import ModelForm
from .models import Post


class CreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')
        labels = {'text': 'Текст',
                  'group': 'Группа'
                  }
