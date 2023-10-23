import uuid
from django.db import models


class Model(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    data_cadastro = models.DateField('Data de Cadastro', auto_now_add=True)
    data_update = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        abstract = True