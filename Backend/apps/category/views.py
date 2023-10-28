from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from apps.utils.pagination import StandardResultsSetPagination
from apps.category.models import Category
from apps.category.serializers import CategorySerializer

    
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    pagination_class = StandardResultsSetPagination
    
    filter_backends = [SearchFilter, OrderingFilter]    
    search_fields =  ['name', 'data_cadastro', 'data_update']
    ordering_fields = ['name', 'data_cadastro', 'data_update']  

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Categoria excluída com sucesso!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def perform_destroy(self, instance):
        instance.delete()
