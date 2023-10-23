from django.db import models
from django.forms import ValidationError
from apps.utils.base_model import Model


class Category(Model):
    name = models.CharField(
        "Categoria",
        max_length=120,
        unique=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        error_messages = {}

        if self.name is None or len(self.name) < 3:
            error_messages[
                "name"
            ] = f"Preencha o nome da categoria, mínimo de 3 caracteres."

        if error_messages:
            raise ValidationError(error_messages)

    class Meta:       
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "category"
