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

  <section class="max-w-6xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
    <h2 class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Cadastrar Fornecedor</h2>

    <form v-on:submit.prevent="submitForm" method="post">
      <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-4">
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="username">Nome Fantasia</label>
          <input id="name" type="text" v-model="name"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Razão Social</label>
          <input id="comapany" type="text" v-model="company_name"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="password">Cnpj</label>
          <input id="text" type="text" v-model="document" maxlength="14"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="contact">Telefones</label>
          <div v-for="(contact, index) in contacts" :key="index">
            <input type="text" v-model="contacts[index].contact" maxlength="11"
              class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring" />
            <button @click="removeContactField(index)" class="text-gray-700 dark:text-gray-200">Remover</button>
          </div>
          <button @click.prevent="addContactField" class="text-gray-700 dark:text-gray-200">Adicionar Telefone</button>
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="passwordConfirmation">Cep</label>
          <input id="a" type="text" v-model="zipcode" maxlength="8"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="username">Rua</label>
          <input id="username" type="text" v-model="street"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Numero</label>
          <input id="emailAddress" type="number" v-model="number"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="password">Complemento</label>
          <input id="password" type="text" v-model="complement"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="passwordConfirmation">Bairro</label>
          <input id="passwordConfirmation" type="text" v-model="neighborhood"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>
        <div>
          <label class="text-gray-700 dark:text-gray-200" for="username">Cidade</label>
          <input id="username" type="text" v-model="city"
            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
        </div>

        <div>
          <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Estado</label>
          <input id="emailAddress" type="text" v-model="state"
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
    <h2 class="text-lg font-medium text-gray-800 dark:text-white">Fornecedores</h2>
    <div class="flex flex-col mt-6">
      <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
        <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
          <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">

            <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
              <thead class="bg-gray-50 dark:bg-gray-800">
                <tr>
                  <th scope="col"
                    class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Nome Fantasia
                  </th>

                  <th scope="col"
                    class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Razão Social
                  </th>

                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    CNPJ
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Telefones
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Endereço
                  </th>
                  <th scope="col"
                    class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                    Ações
                  </th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                <tr v-for="suplier in supliers" v-bind:key="suplier.id">
                  <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                    <div>
                      <h2 class="font-medium text-gray-800 dark:text-white ">{{ suplier.name }}</h2>
                    </div>
                  </td>
                  <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ suplier.company_name }}</h2>
                  </td>
                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ formatCNPJ(suplier.document) }}</h2>
                  </td>
                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white " v-for="contact in suplier.contacts"
                      :key="contact.id">{{ formatContact(contact.contact) }}</h2>
                  </td>

                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <h2 class="font-medium text-gray-800 dark:text-white ">{{ suplier.street }}, {{ suplier.number }}, {{
                      suplier.neighborhood }}, {{ suplier.city }} {{ suplier.state }}</h2>
                    <p class="text-sm font-normal text-gray-600 dark:text-gray-400"></p>
                  </td>

                  <td class="px-4 py-4 text-sm whitespace-nowrap">
                    <div class="flex items-center sm:gap-x-5">
                      <a href="#" @click="editSuplier(suplier)">
                        <h2 class="font-medium text-gray-800 dark:text-white ">Editar</h2>
                      </a>
                      <a href="#" @click="deleteSuplier(suplier.id)">
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
  name: 'SuplierView',
  data() {
    return {
      supliers: [],
      contacts: [],
      contact: '',
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
      successMessage: '',
      errorMessage: '',
      editingSuplierId: null,
      editingSuplier: {},
    };
  },
  components: {},

  mounted() {
    this.getSuplier();
  },

  methods: {
    getSuplier() {
      axios.get('/api/fornecedores/')
        .then(response => {
          this.supliers = response.data;
        })
        .catch(error => {
          console.error('Error fetching supliers', error);
        });
    },

    addSuplier() {
      axios.post('/api/fornecedores/', {
        name: this.name,
        company_name: this.company_name,
        document: this.document,
        zipcode: this.zipcode,
        street: this.street,
        number: this.number,
        complement: this.complement,
        neighborhood: this.neighborhood,
        city: this.city,
        state: this.state,
        contacts: this.contacts
      })
        .then(response => {
          this.successMessage = 'Suplier added successfully';
          this.name = '';
          this.getSuplier();

        })
        .catch(error => {
          this.errorMessage = 'Error adding suplier';
          console.error('Error adding suplier', error);
        });
    },

    updateSuplier(id, updatedSuplier) {
      axios.put(`/api/fornecedores/${id}/`, updatedSuplier)
        .then(response => {
          console.log(response.data)
          this.successMessage = 'Suplier updated successfully';
          this.name = '';
          this.company_name = '';
          this.document = '';
          this.zipcode = '';
          this.street = '';
          this.number = '';
          this.complement = '';
          this.neighborhood = '';
          this.city = '';
          this.state = '';
          this.contacts = '';
          this.getSuplier();
          this.cancelEdit()

        })
        .catch(error => {
          this.errorMessage = 'Error updating suplier';
          console.error('Error updating suplier', error);
        });
    },

    editSuplier(suplier) {
      this.editingSuplierId = suplier.id;
      this.editingSuplier = { ...suplier };
      this.name = suplier.name;
      this.company_name = suplier.company_name;
      this.document = suplier.document;
      this.zipcode = suplier.zipcode;
      this.street = suplier.street;
      this.number = suplier.number;
      this.complement = suplier.complement;
      this.neighborhood = suplier.neighborhood;
      this.city = suplier.city;
      this.state = suplier.state;
      if (suplier.contacts) {
        this.contacts = suplier.contacts.map(contact => ({ contact: contact.contact }));
      } else {
        this.contacts = [{ contact: '' }];
      }

    },

    cancelEdit() {
      this.editingSuplierId = null;
      this.editingSuplier = {};
      this.name = '';
      this.company_name = '';
      this.document = '';
      this.zipcode = '';
      this.street = '';
      this.number = '';
      this.complement = '';
      this.neighborhood = '';
      this.city = '';
      this.state = '';
      this.contacts = [{ contact: '' }]
    },


    deleteSuplier(id) {
      axios.delete(`/api/fornecedores/${id}/`)
        .then(response => {
          this.successMessage = 'Suplier deleted successfully';
          this.getSuplier();
        })
        .catch(error => {
          this.errorMessage = 'Error deleting suplier';
          console.error('Error deleting suplier', error);
        });
    },

    addContactField() {
      const newContact = {
        contact: '',
      };
      this.contacts.push(newContact);
    },

    removeContactField(index) {
      this.contacts.splice(index, 1);
    },

    submitForm() {
      if (this.editingSuplierId) {
        this.updateSuplier(this.editingSuplierId, {
          name: this.name,
          company_name: this.company_name,
          document: this.document,
          zipcode: this.zipcode,
          street: this.street,
          number: this.number,
          complement: this.complement,
          neighborhood: this.neighborhood,
          city: this.city,
          state: this.state,
          contacts: this.contacts.map(contact => ({ contact: contact.contact }))
           });
      } else {
        this.addSuplier();
      }
    },

    formatContact(contact) {
      if (contact.length === 11) {
        return `(${contact.slice(0, 2)}) ${contact.slice(2, 7)}-${contact.slice(7)}`;
      } else {
        return `(${contact.slice(0, 2)}) ${contact.slice(2, 6)}-${contact.slice(6)}`;
      }
    },

    formatCNPJ(cnpj) {
      if (cnpj.length === 14) {
        return `${cnpj.slice(0, 2)}.${cnpj.slice(2, 5)}.${cnpj.slice(5, 8)}/${cnpj.slice(8, 12)}-${cnpj.slice(12)}`;
      }
    },
  },
};
</script>