from rest_framework.serializers import (
    ModelSerializer,
    CharField,
)
from apps.category.models import Category
from apps.suplier.models import Suplier
from apps.suplier.serializers import SuplierSerializer
from apps.category.serializers import CategorySerializer
from apps.product.models import Product, SuplierProduct


class SuplierProductSerializer(ModelSerializer):
    # product = CharField(source="product.name", read_only=True)
    suplier = CharField(source="suplier.name", read_only=False)

    class Meta:
        model = SuplierProduct
        fields = ["id", "suplier", "price"]


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(ModelSerializer):
    supliers = SuplierProductSerializer(many=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "category",
            "supliers",
            "data_cadastro",
            "data_update",
        ]
        

    def create(self, validated_data):
        supliers_data = validated_data.pop("supliers")
        product = Product.objects.create(**validated_data)

        for suplier_data in supliers_data:
            try:
                suplier_name = suplier_data.get("suplier")["name"]
                price = suplier_data.get("price")

                suplier = Suplier.objects.get(name=suplier_name)

                if suplier is not None:
                    SuplierProduct.objects.create(
                        product=product, suplier=suplier, price=price
                    )
            except Suplier.DoesNotExist:
                raise ValueError(f"Fornecedoer com nome {suplier_name} não existe")

        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        category_data = validated_data.get("category")
        if category_data:
            instance.category = category_data
        instance.save()

        if "supliers" in validated_data:
            SuplierProduct.objects.filter(product=instance).delete()
            for suplier_data in validated_data["supliers"]:
                suplier_instance = Suplier.objects.get(
                    name=suplier_data["suplier"]["name"]
                )
                SuplierProduct.objects.create(
                    product=instance,
                    suplier=suplier_instance,
                    price=suplier_data["price"],
                )
       
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        category_instance = instance.category
        if category_instance:
            representation["category"] = CategorySerializer(category_instance).data
        suplierproducts_instance = instance.suplierproducts.all()
        if suplierproducts_instance:
            representation["supliers"] = SuplierProductSerializer(
                suplierproducts_instance, many=True
            ).data
        return representation
