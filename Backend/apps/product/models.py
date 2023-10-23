from django.db import models
from django.forms import ValidationError
from apps.category.models import Category
from apps.suplier.models import Suplier
from apps.utils.base_model import Model


class Product(Model):
    name = models.CharField(
        "Produto",
        max_length=200,
        unique=True,
        error_messages={"unique": "Um produto com este nome já foi Cadastrado."},
    )
    description = models.TextField("Descrição", null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    supliers = models.ManyToManyField(
        Suplier, related_name="products"
    )  # through="SuplierProduct"

    class Meta:
        app_label = 'product'
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "product"
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name}"

    def clean(self):
        error_messages = {}

        if self.name is None or len(self.name) < 3:
            error_messages[
                "name"
            ] = f"O Nome do produto deve ter entre 3 e 200 caractéres."

        if error_messages:
            raise ValidationError(error_messages)


class SuplierProduct(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name="Produto",
        on_delete=models.CASCADE,
        related_name="suplierproducts",
    )
    suplier = models.ForeignKey(
        Suplier,
        verbose_name="Fornecedor",
        on_delete=models.CASCADE,
        related_name="suplierproducts",
    )
    price = models.DecimalField("Preço de Custo", max_digits=9, decimal_places=2)

    class Meta:        
        verbose_name = "Produtos Por Fornecedor"
        db_table = "suplier_product"
        ordering = ["suplier"]

    def __str__(self):
        return f"{self.product.name} - {self.suplier.name} - {self.price}"
