from django.contrib import admin
from apps.suplier.models import  Contact, Suplier


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 2

class SuplierAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'company_name', 'cnpj_format', 'get_contacts'] 
    inlines = (ContactInline,)   

    @admin.display(description='Contatos')
    def get_contacts(self, obj):
        return [contact.format_contact for contact in obj.contacts.all()] 
 
 
admin.site.register(Suplier, SuplierAdmin)


