from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from apps.utils.pagination import StandardResultsSetPagination
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


# TODO : Paginação - Filtros


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(serializer.data)
        return Response(serializer.data)
