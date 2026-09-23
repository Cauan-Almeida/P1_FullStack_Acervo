from django import forms
from django.utils import timezone
from .models import Livro

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano', 'disponivel']

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano is not None:
            ano_atual = timezone.localdate().year
            if ano > ano_atual:
                raise forms.ValidationError(
                    f'O ano de publicação não pode ser no futuro. O ano máximo permitido é {ano_atual}.'
                )
        return ano