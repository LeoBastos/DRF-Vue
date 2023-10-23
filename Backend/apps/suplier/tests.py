
from django.test import TestCase
from django.core.exceptions import ValidationError
from apps.suplier.models import Suplier, Address

# Create your tests here.

class SuplierModelTest(TestCase):
    def test_cnpj_format(self):
        suplier = Suplier.objects.create(
            name="Test Suplier",
            company_name="Test Company",
            document="12345678901234",
            zipcode="12345678",
            street="Test Street",
            number=123,
            neighborhood="Test Neighborhood",
            city="Test City",
            state="Test State",
        )
        self.assertEqual(suplier.cnpj_format(), "12.345.678/9012-34")

    def test_string_representation(self):
        suplier = Suplier.objects.create(
            name="Test Suplier",
            company_name="Test Company",
            document="12345678901234",
            zipcode="12345678",
            street="Test Street",
            number=123,
            neighborhood="Test Neighborhood",
            city="Test City",
            state="Test State",
        )
        self.assertEqual(str(suplier), suplier.name)



class AddressModelTest(TestCase):
    def test_string_representation(self):
        address = Address.objects.create(
            zipcode="12345678",
            street="Test Street",
            number=123,
            complement="Test Complement",
            neighborhood="Test Neighborhood",
            city="Test City",
            state="Test State",
        )
        self.assertEqual(
            str(address), f"{address.neighborhood} - {address.city} - {address.state}"
        )