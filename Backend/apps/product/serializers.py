from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    SerializerMethodField,
)
from apps.suplier.serializers import SuplierSerializer
from apps.category.serializers import CategorySerializer
from apps.product.models import Product, SuplierProduct


class SuplierProductSerializer(ModelSerializer):
    product = CharField(source="product.name", read_only=True)
    suplier = CharField(source="suplier.name", read_only=True)

    class Meta:
        model = SuplierProduct
        fields = ["id", "product", "suplier", "price"]


class ProductSerializer(ModelSerializer):
    suplierproducts = SuplierProductSerializer(many=True)

    class Meta:
        model = Product
        fields = ["id", "name", "description", "category", "suplierproducts"]

    # TODO: Supliers List []
    def create(self, validated_data):
        supliers_data = validated_data.pop("suplierproducts")
        product = Product.objects.create(**validated_data)

        for suplier_data in supliers_data:
            suplier_id = suplier_data.get("suplier")
            price = suplier_data.get("price")
            if suplier_id is not None:
                SuplierProduct.objects.create(
                    product=product, suplier_id=suplier_id, price=price
                )

        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.category = validated_data.get("category", instance.category)
        instance.save()

        if "supliers" in validated_data:
            instance.supliers.clear()
            for suplier_data in validated_data["supliers"]:
                instance.supliers.add(suplier_data)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["category"] = CategorySerializer(instance.category).data
        representation["suplierproducts"] = SuplierProductSerializer(
            instance.suplierproducts.all(), many=True
        ).data
        return representation
