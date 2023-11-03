from django.contrib import admin
from django.utils.formats import number_format
from apps.product.models import Product, SuplierProduct


class SuplierProductInline(admin.TabularInline):
    list_display = ['id', 'product', 'suplier', 'price']
    model = SuplierProduct
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category", "get_supliers"]
    inlines = (SuplierProductInline,)
    fieldsets = [
        (
            "Produto",
            {
                "fields": [
                    "name",
                    "description",
                ]
            },
        ),
        (
            "Categoria",
            {
                "fields": [
                    "category",
                ]
            },
        ),
    ]

    @admin.display(description="Fornecedores")
    def get_supliers(self, obj):
        return " - ".join(
            [
                f"{suplierproduct.suplier.name}: R${number_format(suplierproduct.price)}"
                for suplierproduct in obj.suplierproducts.all()
            ]
        )

    def get_format_brl(self, obj):
        return number_format(obj.obj.fornecedorproduto.preco, decimal_pos=2)


admin.site.register(Product, ProductAdmin)
admin.site.register(SuplierProduct)
