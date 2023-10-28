from rest_framework.viewsets import ModelViewSet
from apps.utils.pagination import StandardResultsSetPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt import authentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from rest_framework.decorators import action
from apps.suplier.models import Contact, Suplier, Address
from apps.suplier.serializers import (
    AddressSerializer,
    ContactSerializer,
    SuplierSerializer,
)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class SuplierViewSet(ModelViewSet):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer
    authentication_classes = (authentication.JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]    
    search_fields =  ['name', 'company_name', 'document', 'contacts__contact']
    ordering_fields = ['name', 'company_name', 'document',]  

    @action(detail=True, methods=['get'])
    def contacts(self, request, pk=None):
        suplier = self.get_object()
        contacts = Contact.objects.filter(suplier=suplier)
        serializer = ContactSerializer(contacts, many=True) 
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {
                    "message": "Fornecedor criado com sucesso!",
                    "suplier": serializer.data,
                },
                status=status.HTTP_201_CREATED,
                headers=headers,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {
                    "message": "Fornecedor atualizado com sucesso!",
                    "suplier": serializer.data,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Fornecedor excluído com sucesso!"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def perform_create(self, serializer):
        serializer.save()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
