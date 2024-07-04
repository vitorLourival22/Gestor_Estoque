from django.urls import path  # type: ignore

from .views import (
  adicionar_embalagens,
  adicionar_local,
  editar_locais,
  inicio,
  listar_embalagens,
  listar_locais,
)

urlpatterns = [
    path('', inicio, name='inicio'),
    # locais
    path('locais/', listar_locais, name='listar_locais'),
    path('locais/adicionar/', adicionar_local, name='adicionar_local'),
    path('embalagem/', listar_embalagens, name='listar_embalagem'),
    path('embalagem/adicionar', adicionar_embalagens, name='adicionar_embalagem'), 
    path('editar_locais/<pk>/', editar_locais, name='editar_locais'),  # noqa: E501
]
