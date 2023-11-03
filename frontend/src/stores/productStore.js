import { defineStore } from 'pinia';

export const useProductStore = defineStore('product', {
  state: () => ({
    productData: {
      category: {
        id: null,
        name: '',
      },
      supliers: [
        {
          id: null,
          suplier: '',
          price: '',
        },
      ],
      editingProductId: null,
      selectedSuplier: null,
      auxSupliers: [],
    },

    successMessage: '',
  }),
  actions: {
    setProductData(product) {
      this.productData = { ...this.productData, ...product }
      this.productData.editingProductId = product.id;
    },

    titleCase(str) {
      return str.toLowerCase().split(' ').map(function (word) {
        return word.replace(word[0], word[0].toUpperCase());
      }).join(' ');
    },
    
    resetFields() {
      this.productData = {
        id: null,
        name: '',
        description: '',
        category: null,
        supliers: null,
      };
      this.auxSupliers = null;
    },
  },
});