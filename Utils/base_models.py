from pickle import TRUE

from django.db import models


class BaseModel(models.Model):
    criado_em = models.DateTimeField(auto_now_add=TRUE)
    atualizado_em = models.DateTimeField(auto_now=TRUE)

    class Meta:
        abstract = True
