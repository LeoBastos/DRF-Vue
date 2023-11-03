from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.suplier.models import Suplier
from apps.utils.pagination import StandardResultsSetPagination
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    
       
    filter_backends = [SearchFilter, OrderingFilter]    
    search_fields = ['name', 'category__name', 'suplierproducts__suplier__name',] 
    ordering_fields = ['name', 'category__name',] 


    # def get(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)        
    #     return Response(serializer.data) 
