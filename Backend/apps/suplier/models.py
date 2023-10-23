from django.db import models
from apps.utils.base_model import Model


class Address(models.Model):
    zipcode = models.CharField("Cep", max_length=8)
    street = models.CharField("Rua", max_length=120)
    number = models.IntegerField("Numero")
    complement = models.CharField("Complemento", max_length=120, blank=True, null=True)
    neighborhood = models.CharField("Bairro", max_length=120)
    city = models.CharField("Cidade", max_length=120)
    state = models.CharField("Estado", max_length=120)

    def __str__(self) -> str:
        return f'{self.neighborhood} - {self.city} - {self.state}'

    # class Meta:
    #     abstract = True


class Suplier(Address, Model):
    name = models.CharField("Nome Fantasia", max_length=120) 
    company_name = models.CharField("Razão Social", max_length=120)
    document = models.CharField("CNPJ", max_length=14, unique=True)   
   
    
    class Meta:
        verbose_name = "Suplier"
        verbose_name_plural = "Supliers"
        db_table = "suplier"

    def __str__(self):
        return f"{self.name}"  

    
    def cnpj_format(self):
        document = self.document
        formatted_cnpj = f"{document[0:2]}.{document[2:5]}.{document[5:8]}/{document[8:12]}-{document[12:]}"
        return formatted_cnpj
    cnpj_format.short_description="CNPJ"


class Contact(models.Model):
    contact = models.CharField("Telefone", max_length=11)
    suplier = models.ForeignKey(Suplier, verbose_name="Fornecedor", on_delete=models.CASCADE, related_name='contacts')
   
    @property
    def format_contact(self):
        if len(self.contact) == 11:
            return f"({self.contact[0:2]}) {self.contact[2:7]}-{self.contact[7:]}"
        else:
            return f"({self.contact[0:2]}) {self.contact[2:6]}-{self.contact[6:]}"

 