from dataclasses import fields
from pyexpat import model

from django import forms

from .models import Categoria, Embalagem, Fornecedor, Local


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local  # noqa: F811
        fields = ['nome', 'tipo']  # noqa: F811


class EmbalagemForm(forms.ModelForm):
    class Meta:
        model = Embalagem  # noqa: F811
        fields = ['nome', 'sigla']  # noqa: F811


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria  # noqa: F811
        fields = ['nome']  # noqa: F811


class FornecedorForm(forms.ModelForm):
    class meta:
        model = Fornecedor  # noqa: F811
        fields = ['nome_social', 'nome_fantasia', 'produtos']  # noqa: F811
