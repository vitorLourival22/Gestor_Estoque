from django.urls import path  # type: ignore

from .views import (
  adicionar_categorias,
  adicionar_embalagens,
  adicionar_local,
  editar_categorias,
  editar_embalagens,
  editar_locais,
  excluir_categorias,
  excluir_embalagens,
  excluir_locais,
  inicio,
  listar_categorias,
  listar_embalagens,
  listar_locais,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    # locais
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagens/', listar_embalagens, name='listar_embalagens'),
    path('embalagens/adicionar', adicionar_embalagens, name='adicionar_embalagens'),  # noqa: E501
    path('editar_locais/<pk>/', editar_locais, name='editar_locais'),
    path('excluir_locais/<pk>/', excluir_locais, name='excluir_locais'),
    path('editar_embalagnes/<pk>/', editar_embalagens, name='editar_embalagens'),  # noqa: E501
    path('excluir_embalagens/<pk>/', excluir_embalagens, name='excluir_embalagens'),   # noqa: E501
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categorias, name='adicionar_categorias'),  # noqa: E501
    path('editar_categorias/<pk>/', editar_categorias, name='editar_categorias'),  # noqa: E501
    path('excluir_categorias/<pk>/', excluir_categorias, name='excluir_categorias'),   # noqa: E501
]
