
<template>
  <!------------ALERT----------------->
  <section class="alert">
    <div v-if="errorMessage"
      class="flex items-center w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800 absolute right-0">
      <div class="flex items-center justify-center w-12 bg-red-500" id="alert">
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

    <div v-if="successMessage" id="alert-dismiss"
      class="flex items-center w-full max-w-sm overflow-hidden bg-white rounded-lg shadow-md dark:bg-gray-800 absolute right-0">
      <div class="flex items-center justify-center w-12 bg-emerald-500" id="alert">
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

  <!------------FORM----------------->
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

  <!------------TABLE----------------->
  <section class="container px-4 py-6 mx-auto">
    <div class="mt-6 md:flex md:items-center md:justify-between">
      <h2 class="text-lg font-medium text-gray-800 dark:text-white">Categorias</h2>
      <div class="relative flex items-center mt-4 md:mt-0">

        <span class="absolute">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"
            class="w-5 h-5 mx-3 text-gray-400 dark:text-gray-600">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
          </svg>
        </span>

        <form>
          <input type="text" placeholder="Pesquisar" @input="filterCategory"
            class="block w-full py-1.5 pr-5 text-gray-700 bg-white border border-gray-200 rounded-lg md:w-80 placeholder-gray-400/70 pl-11 rtl:pr-11 rtl:pl-5 dark:bg-gray-900 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 dark:focus:border-blue-300 focus:ring-blue-300 focus:outline-none focus:ring focus:ring-opacity-40">
        </form>

      </div>
    </div>
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
                    <button class="flex items-center gap-x-3 focus:outline-none" @click="OrderingCategory('name')">
                      <span>Nome</span>

                      <svg class="h-3" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M2.13347 0.0999756H2.98516L5.01902 4.79058H3.86226L3.45549 3.79907H1.63772L1.24366 4.79058H0.0996094L2.13347 0.0999756ZM2.54025 1.46012L1.96822 2.92196H3.11227L2.54025 1.46012Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M0.722656 9.60832L3.09974 6.78633H0.811638V5.87109H4.35819V6.78633L2.01925 9.60832H4.43446V10.5617H0.722656V9.60832Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M8.45558 7.25664V7.40664H8.60558H9.66065C9.72481 7.40664 9.74667 7.42274 9.75141 7.42691C9.75148 7.42808 9.75146 7.42993 9.75116 7.43262C9.75001 7.44265 9.74458 7.46304 9.72525 7.49314C9.72522 7.4932 9.72518 7.49326 9.72514 7.49332L7.86959 10.3529L7.86924 10.3534C7.83227 10.4109 7.79863 10.418 7.78568 10.418C7.77272 10.418 7.73908 10.4109 7.70211 10.3534L7.70177 10.3529L5.84621 7.49332C5.84617 7.49325 5.84612 7.49318 5.84608 7.49311C5.82677 7.46302 5.82135 7.44264 5.8202 7.43262C5.81989 7.42993 5.81987 7.42808 5.81994 7.42691C5.82469 7.42274 5.84655 7.40664 5.91071 7.40664H6.96578H7.11578V7.25664V0.633865C7.11578 0.42434 7.29014 0.249976 7.49967 0.249976H8.07169C8.28121 0.249976 8.45558 0.42434 8.45558 0.633865V7.25664Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.3" />
                      </svg>
                    </button>
                  </th>
                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <button class="flex items-center gap-x-3 focus:outline-none"
                      @click="OrderingCategory('data_cadastro')">
                      <span>Dt Cadastro</span>

                      <svg class="h-3" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M2.13347 0.0999756H2.98516L5.01902 4.79058H3.86226L3.45549 3.79907H1.63772L1.24366 4.79058H0.0996094L2.13347 0.0999756ZM2.54025 1.46012L1.96822 2.92196H3.11227L2.54025 1.46012Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M0.722656 9.60832L3.09974 6.78633H0.811638V5.87109H4.35819V6.78633L2.01925 9.60832H4.43446V10.5617H0.722656V9.60832Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M8.45558 7.25664V7.40664H8.60558H9.66065C9.72481 7.40664 9.74667 7.42274 9.75141 7.42691C9.75148 7.42808 9.75146 7.42993 9.75116 7.43262C9.75001 7.44265 9.74458 7.46304 9.72525 7.49314C9.72522 7.4932 9.72518 7.49326 9.72514 7.49332L7.86959 10.3529L7.86924 10.3534C7.83227 10.4109 7.79863 10.418 7.78568 10.418C7.77272 10.418 7.73908 10.4109 7.70211 10.3534L7.70177 10.3529L5.84621 7.49332C5.84617 7.49325 5.84612 7.49318 5.84608 7.49311C5.82677 7.46302 5.82135 7.44264 5.8202 7.43262C5.81989 7.42993 5.81987 7.42808 5.81994 7.42691C5.82469 7.42274 5.84655 7.40664 5.91071 7.40664H6.96578H7.11578V7.25664V0.633865C7.11578 0.42434 7.29014 0.249976 7.49967 0.249976H8.07169C8.28121 0.249976 8.45558 0.42434 8.45558 0.633865V7.25664Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.3" />
                      </svg>
                    </button>
                  </th>
                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    <button class="flex items-center gap-x-3 focus:outline-none" @click="OrderingCategory('data_update')">
                      <span>Última Atulização</span>

                      <svg class="h-3" viewBox="0 0 10 11" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                          d="M2.13347 0.0999756H2.98516L5.01902 4.79058H3.86226L3.45549 3.79907H1.63772L1.24366 4.79058H0.0996094L2.13347 0.0999756ZM2.54025 1.46012L1.96822 2.92196H3.11227L2.54025 1.46012Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M0.722656 9.60832L3.09974 6.78633H0.811638V5.87109H4.35819V6.78633L2.01925 9.60832H4.43446V10.5617H0.722656V9.60832Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.1" />
                        <path
                          d="M8.45558 7.25664V7.40664H8.60558H9.66065C9.72481 7.40664 9.74667 7.42274 9.75141 7.42691C9.75148 7.42808 9.75146 7.42993 9.75116 7.43262C9.75001 7.44265 9.74458 7.46304 9.72525 7.49314C9.72522 7.4932 9.72518 7.49326 9.72514 7.49332L7.86959 10.3529L7.86924 10.3534C7.83227 10.4109 7.79863 10.418 7.78568 10.418C7.77272 10.418 7.73908 10.4109 7.70211 10.3534L7.70177 10.3529L5.84621 7.49332C5.84617 7.49325 5.84612 7.49318 5.84608 7.49311C5.82677 7.46302 5.82135 7.44264 5.8202 7.43262C5.81989 7.42993 5.81987 7.42808 5.81994 7.42691C5.82469 7.42274 5.84655 7.40664 5.91071 7.40664H6.96578H7.11578V7.25664V0.633865C7.11578 0.42434 7.29014 0.249976 7.49967 0.249976H8.07169C8.28121 0.249976 8.45558 0.42434 8.45558 0.633865V7.25664Z"
                          fill="currentColor" stroke="currentColor" stroke-width="0.3" />
                      </svg>
                    </button>
                  </th>
                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Ações
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">

                <tr v-for="category in categories" v-bind:key="category.id" :data="filterCategory(search)">
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
                      <a href="#" @click="openModal(category)" class="tooltip">
                        <h2 class="font-medium text-gray-800 dark:text-white ">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-eye" viewBox="0 0 16 16">
                            <path
                              d="M16 8s-3-5.5-8-5.5S0 8 0 8s3 5.5 8 5.5S16 8 16 8zM1.173 8a13.133 13.133 0 0 1 1.66-2.043C4.12 4.668 5.88 3.5 8 3.5c2.12 0 3.879 1.168 5.168 2.457A13.133 13.133 0 0 1 14.828 8c-.058.087-.122.183-.195.288-.335.48-.83 1.12-1.465 1.755C11.879 11.332 10.119 12.5 8 12.5c-2.12 0-3.879-1.168-5.168-2.457A13.134 13.134 0 0 1 1.172 8z" />
                            <path
                              d="M8 5.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5zM4.5 8a3.5 3.5 0 1 1 7 0 3.5 3.5 0 0 1-7 0z" />
                          </svg>
                        </h2>
                        <span class="tooltiptext">Visualizar Categoria</span>
                      </a>
                      <a href="#" @click="editCategory(category)" class="tooltip">
                        <h2 class="font-medium text-gray-800 dark:text-white ">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-pencil-square" viewBox="0 0 16 16">
                            <path
                              d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z" />
                            <path fill-rule="evenodd"
                              d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z" />
                          </svg>
                        </h2>
                        <span class="tooltiptext">Editar Categoria</span>
                      </a>
                      <a href="#" @click="deleteCategory(category.id)" class="tooltip">
                        <h2 class="font-medium text-gray-800 dark:text-white">
                          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                            class="bi bi-trash" viewBox="0 0 16 16">
                            <path
                              d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z" />
                            <path
                              d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z" />
                          </svg>
                        </h2>
                        <span class="tooltiptext">Excluir Categoria</span>
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

    <div>
      <Pagination :current-page="currentPage" :total-pages="totalPages" :next="next" :previous="previous"
        @change-page="loadPage" />
    </div>
  </section>

  <!------------MODAL----------------->
  <section>
    <TheModal :show="showModal" @close="closeModal">
      <template #header>
        <h3 class="text-lg font-medium leading-6 text-gray-800  dark:text-white" id="modal-title">
          Detalhes da Categoria
        </h3>
      </template>
      <template #body>
        <div class="grid grid-cols-2 gap-6 mt-4">
          <div>
            <label class="text-gray-700 dark:text-gray-200" for="username">Id</label>
            <input id="id_cat" type="text" disabled v-model="selectedCategory.id"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
          </div>
          <div>
            <label class="text-gray-700 dark:text-gray-200" for="username">Categoria</label>
            <input id="id_name" type="text" disabled v-model="selectedCategory.name"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
          </div>

          <div>
            <label class="text-gray-700 dark:text-gray-200" for="id_dc">Data de Cadastro</label>
            <input id="id_dc" type="text" disabled v-model="selectedCategory.data_cadastro_formatted"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
          </div>

          <div>
            <label class="text-gray-700 dark:text-gray-200" for="password">Ultima Atualização</label>
            <input id="id_du" type="text" maxlength="14" disabled v-model="selectedCategory.data_update_formatted"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
          </div>
        </div>
      </template>
      <template #footer>
        <button
          class="modal-default-button px-8 py-2.5 leading-5 text-sm text-gray-800 transition-colors duration-200  border rounded-lg sm:w-auto dark:hover:bg-gray-600  hover:bg-gray-100 dark:text-white dark:border-gray-700"
          @click="closeModal">Fechar</button>
      </template>
    </TheModal>
  </section>
</template>

<script>
import axios from 'axios';
import { format } from 'date-fns';
import { ptBR } from 'date-fns/locale';
import TheModal from '@/components/TheModal.vue';
import Pagination from '@/components/ThePagination.vue';


export default {
  name: 'CategoryView',
  data() {
    return {
      baseURL: '/api/categorias/',
      categories: [],
      next: null,
      previous: null,
      totalPages: 10,
      currentPage: 1,
      searchCategories: [],
      search: null,
      ordering: null,
      orderDirection: 'asc',
      name: '',
      editingCategoryId: null,
      editingCategory: {},
      successMessage: '',
      errorMessage: '',
      errorTimeout: null,
      successTimeout: null,
      showModal: false,
      selectedCategory: {
        data_cadastro: '',
        data_cadastro_formatted: ''
      }
    };
  },

  components: {
    TheModal,
    Pagination
  },

  watch: {
    errorMessage(newMessage) {
      this.handleMessageUpdate(newMessage, "error");
    },
    successMessage(newMessage) {
      this.handleMessageUpdate(newMessage, "success");
    },
  }, 

  mounted() {
    this.getCategory(this.baseURL);
    this.setTimers();
  },

  methods: {
    
    async getCategory(url) {
      await axios.get(url)
        .then(response => {
          this.categories = response.data.results;
          this.next = response.data.next;
          this.previous = response.data.previous;
          this.totalPages = response.data.total_pages;
        })
        .catch(error => {
          console.error('Error fetching categories', error);
        });
    },

    loadPage(page) {
      this.currentPage = page;
      const url = `${this.baseURL}?page=${page}`;
      this.getCategory(url);
    },

    async addCategory() {
      await axios.post(this.baseURL, { name: this.name })
        .then(response => {
          this.successMessage = 'Categoria adicionada.';
          this.name = '';
          this.getCategory(this.baseURL);
        })
        .catch(error => {
          this.errorMessage = `Erro ao incluir a categoria.`
          console.log(error)
        });
    },

    async updateCategory(id, updatedCategory) {
      await axios.put(`${this.baseURL}${id}/`, updatedCategory)
        .then(response => {
          this.successMessage = 'Categoria Atualizada.';
          this.name = '';
          this.getCategory(this.baseURL);
          this.cancelEdit()

        })
        .catch(error => {
          this.errorMessage = `Erro ao atualizar a categoria.`
          console.error('Error updating category', error);
        });
    },

    async deleteCategory(id) {
      await axios.delete(`${this.baseURL}${id}/`)
        .then(response => {
          this.successMessage = 'Categoria Excluida.';
          this.getCategory(this.baseURL);
        })
        .catch(error => {
          this.errorMessage = `Erro ao excluir a categoria.`
          console.error('Error deleting category', error);
        });
    },

    async created() {
      try {
        const response = await axios.get(this.baseURL);
        this.allCategories = response.data.results;
        this.categories = this.allCategories;
      } catch (error) {
        console.error('Error getting all categories', error);
      }
    },

    async filterCategory(event) {
      if (event && event.target) {
        this.search = event.target.value;
        if (this.search && this.search.length >= 3) {
          try {
            const response = await axios.get(`${this.baseURL}?search=${this.search}`);
            this.categories = response.data.results;
          } catch (error) {
            console.error('Error filter category', error);
          }
        } else if (this.search === '') {
          try {
            const response = await axios.get(this.baseURL);
            this.categories = response.data.results;
          } catch (error) {
            console.error('Error getting all categories', error);
          }
        }
      }
    },

    async OrderingCategory(orderField) {
      this.orderDirection = this.orderDirection === 'asc' ? 'desc' : 'asc';
      this.ordering = this.orderDirection === 'desc' ? `-${orderField}` : orderField;
      await axios.get(`${this.baseURL}?ordering=${this.ordering}`)
        .then(response => {
          this.categories = response.data.results;
          if (this.orderDirection === 'asc') {
            this.categories.sort((a, b) => a[orderField].localeCompare(b[orderField], undefined, { sensitivity: 'accent' }));
          } else {
            this.categories.sort((a, b) => b[orderField].localeCompare(a[orderField], undefined, { sensitivity: 'accent' }));
          }
          console.log(response.data.results);
        })
        .catch(error => {
          console.error('Error ordering category', error);
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

    openModal(category) {
      this.selectedCategory = {
        ...category,
        data_cadastro_formatted: this.formatDate(category.data_cadastro),
        data_update_formatted: this.formatDate(category.data_update)
      };
      this.showModal = true;
    },

    closeModal() {
      this.selectedCategory = {};
      this.showModal = false;
    },

    setTimers() {
      setTimeout(() => {
        this.errorMessage = null;
      }, 2000);
      setTimeout(() => {
        this.successMessage = null;
      }, 2000);
    },

    handleMessageUpdate(newMessage, type) {
      if (newMessage) {
        setTimeout(() => {
          if (type === "error") {
            this.errorMessage = null;
          } else if (type === "success") {
            this.successMessage = null;
          }
        }, 2000);
      }
    },

    displayErrorMessage(message) {
      this.errorMessage = message;
    },

    displaySuccessMessage(message) {
      this.successMessage = message;
    },

  },
};
</script>

<style scoped>
#alert {
  align-self: normal;
}
</style>