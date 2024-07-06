from django.urls import path  # type: ignore

from .views import (
  adicionar_embalagens,
  adicionar_local,
  editar_locais,
  excluir_locais,
  inicio,
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
    path('excluir_locais/<pk>/', excluir_locais, name='excluir_locais'),  # noqa: E501
]
