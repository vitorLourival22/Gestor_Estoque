from pickle import TRUE
from django.db import models

class BaseModel(models.Model):
    data_criacao = models.DateTimeField(
        auto_now_add=TRUE
    )
    data_atualizacao = models.DateTimeField(
        auto_now=TRUE
    )

    class Meta:
        abstract = True