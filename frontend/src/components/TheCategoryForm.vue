<template>
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
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        name: '',
      };
    },
  
    methods: {
      submitForm() {
        if (!this.name) {
          console.log('O campo name não pode estar vazio.');
          return;
        }
  
        console.log('submitForm', this.name);
  
        const requestData = {
          name: this.name
        };
  
        axios
          .post('/api/categorias/', requestData)
          .then(response => {
            console.log('data', response.data);
            this.name = '';
          })
          .catch(error => {
            console.log('error', error);
          });
      },
    },
  };
  </script>
  