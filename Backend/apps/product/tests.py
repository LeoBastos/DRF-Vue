from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory
from apps.product.views import ProductViewSet
from apps.product.models import Product, Category, Suplier, SuplierProduct
from django.core.exceptions import ValidationError
from apps.product.serializers import ProductSerializer



class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.suplier = Suplier.objects.create(
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

    def test_name_validation(self):
        with self.assertRaises(ValidationError) as context:
            Product.objects.create(name="A", category=self.category)
        self.assertTrue('name' in context.exception.error_dict)

    def test_string_representation(self):
        product = Product.objects.create(name="Test Product", category=self.category)
        self.assertEqual(str(product), product.name)


class SuplierProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.suplier = Suplier.objects.create(
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
        self.product = Product.objects.create(name="Test Product", category=self.category)

    def test_string_representation(self):
        suplier_product = SuplierProduct.objects.create(
            product=self.product, suplier=self.suplier, price=12.34
        )
        self.assertEqual(
            str(suplier_product),
            f"{self.product.name} - {self.suplier.name} - {suplier_product.price}",
        )


class ProductViewSetTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.product = Product.objects.create(name="Test Product")

    def test_get_product(self):
        request = self.factory.get('/api/products/')
        view = ProductViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, ProductSerializer(Product.objects.all(), many=True).data)