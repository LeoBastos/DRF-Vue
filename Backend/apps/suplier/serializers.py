from django.forms import CharField
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)
from apps.suplier.models import Address, Contact, Suplier


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "zipcode",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
        ]
        # abstract = True


class ContactSerializer(ModelSerializer):
    suplier = SerializerMethodField()

    class Meta:
        model = Contact
        fields = "__all__"

    def get_suplier(self, obj):
        return obj.suplier.name if obj.suplier else None

# TODO
##  Validador de  CNPJ
class SuplierSerializer(ModelSerializer):
    contacts = ContactSerializer(many=True)

    class Meta:
        model = Suplier
        fields = [
            "id",
            "name",
            "company_name",
            "document",
            "zipcode",
            "street",
            "number",
            "complement",
            "neighborhood",
            "city",
            "state",
            "contacts",
        ]
        depth = 1

    def validate_document(self, value):
        if len(value) != 14:
            raise ValidationError("O campo CNPJ deve ter 14 dígitos.")
        return value

    def create(self, validated_data):
        contacts_data = validated_data.pop("contacts")
        suplier = Suplier.objects.create(**validated_data)
        for contact_data in contacts_data:
            Contact.objects.create(suplier=suplier, **contact_data)
        return suplier

    def update(self, instance, validated_data):
        contacts_data = validated_data.pop("contacts")
        contacts = (instance.contacts).all()
        contacts = list(contacts)

        instance.name = validated_data.get("name", instance.name)
        instance.company_name = validated_data.get(
            "company_name", instance.company_name
        )
        instance.document = validated_data.get("document", instance.document)
        instance.zipcode = validated_data.get("zipcode", instance.zipcode)
        instance.street = validated_data.get("street", instance.street)
        instance.number = validated_data.get("number", instance.number)
        instance.complement = validated_data.get("complement", instance.complement)
        instance.neighborhood = validated_data.get(
            "neighborhood", instance.neighborhood
        )
        instance.city = validated_data.get("city", instance.city)
        instance.state = validated_data.get("state", instance.state)
        instance.save()

        for contact_data in contacts_data:
            if contacts:
                contact = contacts.pop(0)
                contact.contact = contact_data.get("contact", contact.contact)
                contact.save()

        return instance
