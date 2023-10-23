from django.test import TestCase
from apps.category.models import Category
from django.core.exceptions import ValidationError


class CategoryModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Category.objects.create(name='Test Category')

    def test_category_creation(self):
        category = Category.objects.create(name='Another Category')
        self.assertEqual(category.name, 'Another Category')

    def test_category_str_representation(self):
        category = Category.objects.get(name='Test Category')
        self.assertEqual(str(category), 'Test Category')

    def test_category_clean_method_with_valid_name(self):
        category = Category(name='Valid Name')
        category.clean()  # This should not raise a ValidationError

    def test_category_clean_method_with_invalid_name(self):
        category = Category(name='A')
        with self.assertRaises(ValidationError):
            category.clean()

  