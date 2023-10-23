
<template>
  <section>
    <div v-if="errorMessage"
      class="flex items-center w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800 absolute right-0">
      <div class="flex items-center justify-center w-12 bg-red-500">
        <svg class="w-12 h-12 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M20 3.36667C10.8167 3.36667 3.3667 10.8167 3.3667 20C3.3667 29.1833 10.8167 36.6333 20 36.6333C29.1834 36.6333 36.6334 29.1833 36.6334 20C36.6334 10.8167 29.1834 3.36667 20 3.36667ZM19.1334 33.3333V22.9H13.3334L21.6667 6.66667V17.1H27.25L19.1334 33.3333Z" />
        </svg>
      </div>

      <div class="px-4 py-2 -mx-3">
        <div class="mx-3">
          <span class="font-semibold text-red-500 dark:text-red-400">Error</span>
          <p class="text-sm text-gray-600 dark:text-gray-200">{{ errorMessage }}</p>
        </div>
      </div>
    </div>

    <div v-if="successMessage"
      class="flex items-center w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800 absolute right-0">
      <div class="flex items-center justify-center w-12 bg-emerald-500">
        <svg class="w-6 h-6 text-white fill-current" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z" />
        </svg>
      </div>

      <div class="px-4 py-2 -mx-3">
        <div class="mx-3">
          <span class="font-semibold text-red-500 dark:text-emerald-400">Success</span>
          <p class="text-sm text-gray-600 dark:text-gray-200">{{ successMessage }}</p>
        </div>
      </div>
    </div>

  </section>


  <section class="max-w-4xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
    <h2 class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Cadastrar Categoria</h2>

    <form v-on:submit.prevent="submitForm" method="post">
      <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="category">Categoria</label>
          <input id="category" type="text" v-model="name"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>
      </div>

      <div class="flex justify-start mt-6">
        <button
          class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">Cadastrar</button>
      </div>
    </form>
  </section>

  <section class="container px-4 py-6 mx-auto">
    <h2 class="text-lg font-medium text-gray-800 dark:text-white">Categorias</h2>
    <div class="flex flex-col mt-6">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">

            <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
              <thead class="bg-gray-50 dark:bg-gray-800">
                <tr>
                  <th scope="col"
                    class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Id
                  </th>

                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Nome
                  </th>
                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Dt. Cadastro
                  </th>
                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Ultima Atulização
                  </th>
                  <th scope="col"
                    class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Ação
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">

                <tr v-for="category in categories" v-bind:key="category.id">
                  <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                    <div>
                      <h2 class="font-medium text-gray-800 dark:text-white ">{{ category.id }}</h2>
                    </div>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ category.name }}</h2>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ formatDate(category.data_cadastro) }}</h2>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ formatDate(category.data_update) }}</h2>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <div class="flex items-center sm:gap-x-5">
                      <a href="#" @click="editCategory(category)">
                        <h2 class="font-medium text-gray-800 dark:text-white ">Editar</h2>
                      </a>
                      <a href="#" @click="deleteCategory(category.id)">
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
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';

export default {
  name: 'CategoryView',
  data() {
    return {
      categories: [],
      name: '',
      successMessage: '',
      errorMessage: '',
      editingCategoryId: null,
      editingCategory: {},
    };
  },
  components: {},

  mounted() {
    this.getCategory();
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

    addCategory() {
      axios.post('/api/categorias/', { name: this.name })
        .then(response => {
          this.successMessage = 'Category added successfully';
          this.name = '';
          this.getCategory();

        })
        .catch(error => {
          this.errorMessage = 'Error adding category';
          console.error('Error adding category', error);
        });
    },

    updateCategory(id, updatedCategory) {
      axios.put(`/api/categorias/${id}/`, updatedCategory)
        .then(response => {
          this.successMessage = 'Category updated successfully';
          this.name = '';
          this.getCategory();
          this.cancelEdit()

        })
        .catch(error => {
          this.errorMessage = 'Error updating category';
          console.error('Error updating category', error);
        });
    },

    deleteCategory(id) {
      axios.delete(`/api/categorias/${id}/`)
        .then(response => {
          this.successMessage = 'Category deleted successfully';
          this.getCategory();
        })
        .catch(error => {
          this.errorMessage = 'Error deleting category';
          console.error('Error deleting category', error);
        });
    },

    editCategory(category) {
      this.editingCategoryId = category.id;
      this.editingCategory = { ...category };
      this.name = category.name;
    },
    cancelEdit() {
      this.editingCategoryId = null;
      this.editingCategory = {};
      this.name = '';
    },

    submitForm() {
      if (this.editingCategoryId) {
        this.updateCategory(this.editingCategoryId, { name: this.name });
      } else {
        this.addCategory();
      }
    },

    formatDate(date) {
      return format(new Date(date), 'dd/MM/yyyy', { locale: ptBR });
    },
  },
};
</script>


<!-- <script>
import axios from 'axios'
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';
// import TheCategoryForm from '../components/TheCategoryForm.vue'

export default {
  name: 'CategoryView',
  data() {
    return {
      categories: [],
      body: '',
      name: '',
      successMessage: '',
      errorMessage: ''
    }
  },
  components: { // TheCategoryForm
  },
  mounted() {
    this.getCategory()
  },

  methods: {
    submitForm() {
      if (!this.name) {
        this.errorMessage = 'O campo name não pode estar vazio.';
        return;
      }

      const requestData = {
        name: this.name
      };

      axios
        .post('/api/categorias/', requestData)
        .then(response => {
          this.successMessage = 'Categoria criada com sucesso.';
          this.name = '';
          this.getCategory(); // Atualiza a lista de categorias após adicionar com sucesso
        })
        .catch(error => {
          this.errorMessage = 'Erro ao criar categoria.';
          console.log('error', error);
        });
    },

    getCategory() {
      axios
        .get('/api/categorias/')
        .then(response => {
          this.categories = response.data
        })
        .catch(error => {
          this.errorMessage = 'Erro ao carregar categorias.';
          console.log('error', error)
        })
    },
    editCategory(id) {
      // Redireciona para a rota de edição com o ID da categoria
      this.$router.push({ name: 'EditCategory', params: { id: id } });
    },

    deleteCategory(id) {
      if (confirm('Tem certeza que deseja excluir esta categoria?')) {
        axios
          .delete(`/api/categorias/${id}/`)
          .then(response => {
            this.successMessage = 'Categoria excluída com sucesso.';
            this.getCategory();
          })
          .catch(error => {
            this.errorMessage = 'Erro ao excluir categoria.';
            console.error('Erro ao excluir categoria', error);
          });
      }
    },
    formatDate(date) {
      return format(new Date(date), 'dd/MM/yyyy', { locale: ptBR });
    },
  },
}
</script> -->