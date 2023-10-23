<template>
  <section class="max-w-6xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
    <h2 class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Cadastrar Produto</h2>

    <form v-on:submit.prevent="submitForm" method="post">
      <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="username">Produto</label>
          <input id="username" type="text" v-model="name"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="category">Categoria</label>
          <select v-model="selectedCategory" id="category" @change="categoryChanged"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
            <option v-for="product in products" :value="product.id" :key="product.id">
              {{ product.category.name }}
            </option>
          </select>
        </div>
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="suplier">Fornecedor</label>
          <select v-model="selectedSuplier" id="suplier"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
            <option v-for="suplier in supliers" :value="suplier.id" :key="suplier.id">
              {{ suplier.name }}
            </option>
          </select>
        </div>


        <div>
          <label class="text-gray-700 dark:text-gray-200" for="passwordConfirmation">Preço</label>
          <input id="username" type="text" v-model="price"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>
      </div>
      <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-1">
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Descrição</label>
          <textarea rows="3" v-model="description"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"></textarea>
        </div>
      </div>

      <div class="flex justify-start mt-6">
        <button
          class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">Cadastrar</button>
      </div>
    </form>
  </section>

  <section class="container px-4 py-6 mx-auto">
    <h2 class="text-lg font-medium text-gray-800 dark:text-white">Produtos</h2>
    <div class="flex flex-col mt-6">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">

            <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
              <thead class="bg-gray-50 dark:bg-gray-800">
                <tr>
                  <th scope="col"
                    class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Produto
                  </th>

                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Descrição
                  </th>

                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Categoria
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Fornecedor
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Preço
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Ações
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                <tr v-for="product in products" :key="product.id">
                  <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                    <div>
                      <h2 class="font-medium text-gray-800 dark:text-white ">{{ product.name }}</h2>
                      <p class="text-sm font-normal text-gray-600 dark:text-gray-400"></p>
                    </div>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">
                      {{ product.description || '-' }}
                    </h2>
                  </td>
                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">
                      {{ product.category ? product.category.name : '-' }}
                    </h2>
                  </td>
                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white"
                      v-for="suplierProduct in product.suplierproducts" :key="suplierProduct.id">{{
                        suplierProduct.suplier }}</h2>

                  </td>

                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white "
                      v-for="suplierProduct in product.suplierproducts" :key="suplierProduct.id">R$ {{
                        suplierProduct.price }}</h2>
                  </td>

                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <div class="flex items-center sm:gap-x-5">
                      <a href="#">
                        <h2 class="font-medium text-gray-800 dark:text-white ">Editar</h2>
                      </a>
                      <a href="#">
                        <h2 class="font-medium text-gray-800 dark:text-white ">Excluir</h2>
                      </a>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
import axios from 'axios';

export default {
  name: 'ProductView',
  data() {
    return {
      products: [],
      name: '',
      description: '',
      category: '',
      supliers: [],
      successMessage: '',
      errorMessage: '',
      editingProductId: null,
      editingProduct: {},
      selectedCategory: null,
      selectedSuplier: null,
    };
  },
  computed: {
    selectedCategorySupliers() {
      const selectedProduct = this.products.find(product => product.id === this.selectedCategory);
      return selectedProduct ? selectedProduct.suplierproducts : [];
    }
  },
  components: {},

  mounted() {
    this.getProduct();
    this.getCategory();
    this.getSupliers();
  },

  methods: {
    getCategory() {
      axios.get('/api/categorias/')
        .then(response => {
          this.categories = response.data;
        })
        .catch(error => {
          console.error('Error fetching categories', error);
        });
    },

    getProduct() {
      axios.get('/api/produtos/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products', error);
        });
    },

    getSupliers() {
      axios.get('/api/fornecedores/')
        .then(response => {
          this.supliers = response.data;
        })
        .catch(error => {
          console.error('Error fetching supliers', error);
        });
    },

    addProduct() {
      axios.post('/api/produtos/', {
        name: this.name,
        description: this.description,
        category: this.category,
        supliers: this.suplier,
      })
        .then(response => {
          this.successMessage = 'Product added successfully';
          this.name = '';
          this.getProduct();

        })
        .catch(error => {
          this.errorMessage = 'Error adding product';
          console.error('Error adding product', error);
        });
    },

    updateProduct(id, updatedProduct) {
      axios.put(`/api/produtos/${id}/`, updatedProduct)
        .then(response => {
          this.successMessage = 'Product updated successfully';
          this.name = '';
          this.getProduct();
          this.cancelEdit()

        })
        .catch(error => {
          this.errorMessage = 'Error updating product';
          console.error('Error updating product', error);
        });
    },

    deleteProduct(id) {
      axios.delete(`/api/produtos/${id}/`)
        .then(response => {
          this.successMessage = 'Product deleted successfully';
          this.getProduct();
        })
        .catch(error => {
          this.errorMessage = 'Error deleting product';
          console.error('Error deleting product', error);
        });
    },

    editProduct(product) {
      this.editingProductId = product.id;
      this.editingProduct = { ...product };   
      this.name = product.name;
      this.description = product.description;
      this.category = product.category;
      this.supliers = product.suplier;
    },
    cancelEdit() {
      this.editingProductId = null;
      this.editingProduct = {};
      this.name = '';
      this.description = '';
      this.category = '';
      this.supliers = '';
    },

    categoryChanged() {
      this.selectedSuplier = null;
    },

    submitForm() {
      if (this.editingProductId) {
        this.updateProduct(this.editingProductId, { 
          name: this.name,         
          description: this.description,
          category: this.category,
          supliers: this.suplier,
        });
      } else {
        this.addProduct();
      }
    },
  },
};
</script>
