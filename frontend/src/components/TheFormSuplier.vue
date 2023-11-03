<template>

    <TheAlert :message="alertStore.message" :type="alertStore.type" />

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
                    <label class="text-gray-700 dark:text-gray-200" for="numerolabel">Número</label>
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
                    class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600"
                    >
                    {{ suplierStore.suplierData.id ? 'Atualizar' : 'Cadastrar' }}
                </button>
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
import { useAlertStore } from '@/stores/alertStore';
import { useRouter } from 'vue-router';
import TheAlert from '@/components/TheAlert.vue';

export default {
    name: 'TheFormSuplier',
    setup() {
        const suplierStore = useSuplierStore();              
        const router = useRouter();
        const alertStore = useAlertStore();
        let isAlertVisible = ref(false);

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
                alertStore.showAlert('Fornecedor cadastrar com sucesso', 'success')
                suplierStore.resetFields();
                router.replace('/suplier');
            } catch (error) {
                alertStore.showAlert('Erro ao cadastrar fornecedor', 'error')
                console.error('Error adding suplier', error);
            }
        };

        const updateSuplier = async (id, updatedSuplier) => {
            try {
                const response = await axios.put(`/api/fornecedores/${id}/`, updatedSuplier);     
                suplierStore.setSuplierData(response.data);
                alertStore.showAlert('Fornecedor atualizado com sucesso', 'success')
                suplierStore.resetFields();
                router.replace('/suplier');
            } catch (error) {
                alertStore.showAlert('Erro ao cadastrar fornecedor.', 'error')
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
            submitForm,
            getCep,
            addContactField,
            removeContactField,
            suplierStore,
            alertStore,
            isAlertVisible
        };
    },
    components: {
        TheAlert
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
