<template>
    <!------------ALERT----------------->
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

    <!------------FORM----------------->
    <section class="max-w-6xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
        <h2 class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Cadastrar Fornecedor</h2>
        <form v-on:submit.prevent="submitForm" method="post">
            <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-4">
                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="username">Nome Fantasia</label>
                    <input id="name" type="text" v-model="suplierStore.suplierData.name"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="emailAddress">Razão Social</label>
                    <input id="comapany" type="text" v-model="suplierStore.suplierData.company_name"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="password">Cnpj</label>
                    <input id="number" type="text" v-model="suplierStore.suplierData.document" @input="handleCNPJInput"
                        maxlength="14"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring" />
                </div>

                <div>
                    <label for="contact" class="text-gray-700 dark:text-gray-200">Telefones &nbsp &nbsp</label>
                    <div v-for="(contact, index) in suplierStore.suplierData.contacts" :key="index">
                        <input type="text" v-model="contact.contact" maxlength="11" @input="handleContactInput"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring" />
                        <button @click="removeContactField(index)" class="text-gray-700 dark:text-gray-200">Remover</button>
                    </div>
                    <button @click.prevent="addContactField" class="text-gray-700 dark:text-gray-200">Adicionar</button>
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="cep">Cep</label>
                    <input id="zipcode" type="text" v-model="suplierStore.suplierData.zipcode" maxlength="8"
                        @input="handleZipCodeInput" v-on:blur="getCep(this.zipcode)"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>
                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="rua">Rua</label>
                    <input id="rua" type="text" v-model="suplierStore.suplierData.street"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="numerolabel">Numero</label>
                    <input id="numero" type="number" v-model="suplierStore.suplierData.number"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="complement">Complemento</label>
                    <input id="complemento" type="text" v-model="suplierStore.suplierData.complement"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="bairro">Bairro</label>
                    <input id="bairro" type="text" v-model="suplierStore.suplierData.neighborhood"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>
                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="cidade">Cidade</label>
                    <input id="cidade" type="text" v-model="suplierStore.suplierData.city"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>

                <div>
                    <label class="text-gray-700 dark:text-gray-200" for="estado">Estado</label>
                    <input id="estado" type="text" v-model="suplierStore.suplierData.state"
                        class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                </div>
            </div>

            <div class="flex justify-start space-x-4 mt-6">
                <button
                    class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">Cadastrar</button>
                <RouterLink to="/suplier"
                    class="px-8 py-2.5 leading-5 text-sm text-gray-800 transition-colors duration-200  border rounded-lg sm:w-auto dark:hover:bg-gray-600  hover:bg-gray-100 dark:text-white dark:border-gray-700">
                    Voltar</RouterLink>
            </div>
        </form>
    </section>
</template>
    

<script>
import axios from 'axios';
import { ref } from 'vue';
import { useSuplierStore } from '@/stores/suplierStore';
import { useRouter } from 'vue-router';

export default {
    name: 'TheFormSuplier',
    setup() {
        const suplierStore = useSuplierStore();
        const successMessage = ref('');
        const errorMessage = ref('');
        const router = useRouter();

        const addContactField = (newContact) => {
            suplierStore.addContactField(newContact);
        };

        const removeContactField = (index) => {
            suplierStore.removeContactField(index);
        };

        const addSuplier = async (suplierData) => {
            try {
                const response = await axios.post('/api/fornecedores/', suplierData);
                suplierStore.setSuplierData(suplierData);
                suplierStore.successMessage = 'Fornecedor cadastrado.';
                suplierStore.resetFields();
                router.replace('/suplier');
            } catch (error) {
                errorMessage.value = 'Erro ao cadastrar fornecedor.';
                console.error('Error adding suplier', error);
            }
        };

        const updateSuplier = async (id, updatedSuplier) => {
            try {
                const response = await axios.put(`/api/fornecedores/${id}/`, updatedSuplier);
                suplierStore.setSuplierData(response.data);
                successMessage.value = 'Fornecedor atualizado com sucesso';
                suplierStore.resetFields();
                router.replace('/suplier');
            } catch (error) {
                errorMessage.value = 'Erro ao cadastrar fornecedor.';
                console.error('Error adding suplier', error);
            }
        };

        const submitForm = () => {
            const suplierData = {
                name: suplierStore.suplierData.name,
                company_name: suplierStore.suplierData.company_name,
                document: suplierStore.suplierData.document,
                zipcode: suplierStore.suplierData.zipcode,
                street: suplierStore.suplierData.street,
                number: suplierStore.suplierData.number,
                complement: suplierStore.suplierData.complement,
                neighborhood: suplierStore.suplierData.neighborhood,
                city: suplierStore.suplierData.city,
                state: suplierStore.suplierData.state,
                contacts: [...suplierStore.suplierData.contacts],
            };

            if (suplierStore.suplierData.editingSuplierId) {
                updateSuplier(suplierStore.suplierData.editingSuplierId, suplierData);
            } else {
                addSuplier(suplierData);
            }
        };

        const getCep = async (zipcode) => {
            try {
                const response = await axios.get(`https://viacep.com.br/ws/${suplierStore.suplierData.zipcode}/json`);
                suplierStore.suplierData.street = response.data.logradouro;
                suplierStore.suplierData.number = response.data.numero;
                suplierStore.suplierData.neighborhood = response.data.bairro;
                suplierStore.suplierData.city = response.data.localidade;
                suplierStore.suplierData.state = response.data.uf;
            } catch (error) {
                console.error('Erro ao buscar os dados do cep', error);
            }
        };

        return {
            successMessage,
            errorMessage,
            submitForm,
            getCep,
            addContactField,
            removeContactField,
            suplierStore,
        };
    },
    methods: {
        handleCNPJInput(event) {
            // Filtrar caracteres não numéricos
            const formattedCNPJ = event.target.value.replace(/\D/g, '');
            // Limitar a 14 dígitos
            this.suplierStore.suplierData.document = formattedCNPJ.slice(0, 14);
        },

        handleContactInput(event, index) {
            const contactFormat = event.target.value.replace(/\D/g, '');
            if (this.suplierStore.suplierData.contacts[index]) {
                this.suplierStore.suplierData.contacts[index].contact = contactFormat.slice(0, 11);
            }
        },

        handleZipCodeInput(event) {
            // Filtrar caracteres não numéricos
            const zipcodeFormat = event.target.value.replace(/\D/g, '');
            // Limitar a 14 dígitos
            this.suplierStore.suplierData.zipcode = zipcodeFormat.slice(0, 8);
        },
    }
};
</script>
