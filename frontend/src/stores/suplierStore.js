import { defineStore } from 'pinia';


export const useSuplierStore = defineStore('suplier', {
  state: () => ({
    suplierData: {
      contacts: [],
      editingSuplierId: null,
    },
    successMessage: '',
  }),
  actions: {
    addContactField() {
      this.suplierData.contacts.push({ contact: '' });
    },
    removeContactField(index) {
      this.suplierData.contacts.splice(index, 1);
    },
    setSuplierData(suplier) {
      this.suplierData = { ...this.suplierData, ...suplier };
      this.suplierData.editingSuplierId = suplier.id;
    },    

    resetFields() {
      this.suplierData = {
        name: '',
        company_name: '',
        document: '',
        zipcode: '',
        street: '',
        number: '',
        complement: '',
        neighborhood: '',
        city: '',
        state: '',
        contacts: [],
      };
    },
  },
});