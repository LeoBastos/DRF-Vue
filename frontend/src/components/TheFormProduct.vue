<template>
    <TheAlert v-if="isAlertVisible" :message="alertStore.message" :type="alertStore.type" />
    <!------------FORM----------------->
    <section class="max-w-6xl  p-6 mt-6 mx-auto bg-white rounded-md shadow-md dark:bg-gray-800">
        <h2 v-if="!editingProductId" class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Cadastrar
            Produto</h2>
        <h2 v-else class="text-lg font-semibold text-gray-700 capitalize dark:text-white">Atualizar Produto</h2>

        <form v-on:submit.prevent="submitForm" method="post">

            <div v-if="!editingProductId">
                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="product">Produto</label>
                        <input id="product" type="text" v-model="productStore.productData.name"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                    </div>
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="category">Categoria</label>
                        <select id="category" @change="categoryChanged"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                            <option value="">----</option>
                            <option v-for="category in categories" :value="category.id" :key="category.id">
                                {{ category.name }}
                            </option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-1">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="description">Descrição</label>
                        <textarea rows="3" v-model="productStore.productData.description"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"></textarea>
                    </div>
                </div>
                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-3">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="suplier">Fornecedor</label>
                        <select v-model="selectedSuplier" id="suplier"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                            <option v-for="suplier in supliers" :value="suplier ? suplier.id : ''"
                                :key="suplier ? suplier.id : ''">
                                {{ suplier ? suplier.name : '' }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="price">Preço</label>
                        <input id="price" type="text" v-model="price"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                    </div>
                    <div class="plus">
                        <button @click.prevent="addAuxSuplierAndPrice()"
                            class="px-8 py-2.5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-plus-lg" viewBox="0 0 16 16">
                                <path fill-rule="evenodd"
                                    d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2Z" />
                            </svg>
                        </button>
                    </div>
                </div>
            </div>

            <div v-else>
                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-2">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="product">Produto</label>
                        <input id="product" type="text" v-model="productStore.productData.name"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring" />
                    </div>
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="category">Categoria</label>
                        <select id="category" type="text" @change="categoryChanged"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                            <option v-for="category in categories" :value="category.id" :key="category.id">
                                {{ category.name }}
                            </option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-1">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="description">Descrição</label>
                        <textarea rows="3" v-model="productStore.productData.description"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring"></textarea>
                    </div>
                </div>


                <div class="grid grid-cols-1 gap-6 mt-4 sm:grid-cols-3">
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="suplier">Fornecedor</label>
                        <select v-model="selectedSuplier" id="suplier"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                            <option v-for="suplier in supliers" :value="suplier ? suplier.id : ''"
                                :key="suplier ? suplier.id : ''">
                                {{ suplier ? suplier.name : '' }}
                            </option>
                        </select>
                    </div>
                    <div>
                        <label class="text-gray-700 dark:text-gray-200" for="price">Preço</label>
                        <input id="price" type="text" v-model="price"
                            class="block w-full px-4 py-2 mt-2 text-gray-700 bg-white border border-gray-200 rounded-md dark:bg-gray-800 dark:text-gray-300 dark:border-gray-600 focus:border-blue-400 focus:ring-blue-300 focus:ring-opacity-40 dark:focus:border-blue-300 focus:outline-none focus:ring">
                    </div>
                    <div class="plus">
                        <button @click.prevent="addAuxSuplierAndPrice()"
                            class="px-8 py-2.5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">
                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor"
                                class="bi bi-plus-lg" viewBox="0 0 16 16">
                                <path fill-rule="evenodd"
                                    d="M8 2a.5.5 0 0 1 .5.5v5h5a.5.5 0 0 1 0 1h-5v5a.5.5 0 0 1-1 0v-5h-5a.5.5 0 0 1 0-1h5v-5A.5.5 0 0 1 8 2Z" />
                            </svg>
                        </button>
                    </div>
                </div>

            </div>


            <div class="flex justify-start mt-6">
                <button type="submit"
                    class="px-8 py-2.5 leading-5 text-white transition-colors duration-300 transform bg-gray-700 rounded-md hover:bg-gray-600 focus:outline-none focus:bg-gray-600">
                    {{ editingProductId ? 'Atualizar' : 'Cadastrar' }}</button>
            </div>
        </form>
        <hr class="mt-6" />

        <!------------TABELA----------------->
        <div class="flex flex-col mt-6">
            <div class="-mx-4 -my-2 overflow-x-auto sm:-mx-6 lg:-mx-8">
                <div class="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
                    <div class="overflow-hidden border border-gray-200 dark:border-gray-700 md:rounded-lg">
                        <div v-if="!editingProductId">
                            <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead class="bg-gray-50 dark:bg-gray-800">
                                    <tr>
                                        <th scope="col"
                                            class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Fornecedor
                                        </th>

                                        <th scope="col"
                                            class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Preço
                                        </th>
                                        <th scope="col"
                                            class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Ações
                                        </th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                                    <tr v-for="(auxSuplier, index) in auxSupliers" :key="index">
                                        <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                            <div>
                                                <h2 class="font-medium text-gray-800 dark:text-white ">{{ auxSuplier.suplier
                                                }}
                                                </h2>
                                                <p class="text-sm font-normal text-gray-600 dark:text-gray-400"></p>
                                            </div>
                                        </td>
                                        <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                                            <h2 class="font-medium text-gray-800 dark:text-white ">
                                                {{ auxSuplier.price.toLocaleString('pt-BR', {
                                                    style: 'currency', currency: 'BRL'
                                                }) }}
                                            </h2>
                                        </td>
                                        <td class="px-4 py-4 text-sm whitespace-nowrap">
                                            <div class="flex items-center sm:gap-x-5">
                                                <a href="#" @click="removeAuxSuplierAndPrice(index)">
                                                    <h2 class="font-medium text-gray-800 dark:text-white">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                            fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                            <path
                                                                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z" />
                                                            <path
                                                                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z" />
                                                        </svg>
                                                    </h2>
                                                </a>
                                            </div>
                                        </td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                        <div v-else>
                            <table class="min-w-full divide-y divide-gray-200 dark:divide-gray-700">
                                <thead class="bg-gray-50 dark:bg-gray-800">
                                    <tr>
                                        <th scope="col"
                                            class="py-3.5 px-4 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Fornecedor
                                        </th>

                                        <th scope="col"
                                            class="px-12 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Preço
                                        </th>
                                        <th scope="col"
                                            class="px-4 py-3.5 text-sm font-normal text-left rtl:text-right text-gray-500 dark:text-gray-400">
                                            Ações
                                        </th>
                                    </tr>
                                </thead>
                                <tbody class="bg-white divide-y divide-gray-200 dark:divide-gray-700 dark:bg-gray-900">
                                    <tr v-for="(auxSuplier, index) in auxSupliers" :key="index">
                                        <td class="px-4 py-4 text-sm font-medium whitespace-nowrap">
                                            <div>
                                                <h2 class="font-medium text-gray-800 dark:text-white ">{{ auxSuplier.suplier
                                                }}
                                                </h2>
                                                <p class="text-sm font-normal text-gray-600 dark:text-gray-400"></p>
                                            </div>
                                        </td>
                                        <td class="px-12 py-4 text-sm font-medium whitespace-nowrap">
                                            <h2 class="font-medium text-gray-800 dark:text-white ">
                                                {{ auxSuplier.price }}
                                            </h2>
                                        </td>
                                        <td class="px-4 py-4 text-sm whitespace-nowrap">
                                            <div class="flex items-center sm:gap-x-5">
                                                <a href="#" @click="removeAuxSuplierAndPrice(index)">
                                                    <h2 class="font-medium text-gray-800 dark:text-white">
                                                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                                                            fill="currentColor" class="bi bi-trash" viewBox="0 0 16 16">
                                                            <path
                                                                d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5Zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6Z" />
                                                            <path
                                                                d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1ZM4.118 4 4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118ZM2.5 3h11V2h-11v1Z" />
                                                        </svg>
                                                    </h2>
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
        </div>

    </section>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import TheAlert from './TheAlert.vue';
import { useAlertStore } from '@/stores/alertStore';
import { useProductStore } from '@/stores/productStore';
import { useRouter } from 'vue-router';

export default {
    name: 'TheFormProduct',
    data() {
        return {
            baseURL: '/api/produtos/',
            baseURLCategory: '/api/categorias/',
            baseURLSuplier: '/api/fornecedores/',
            message: '',
            type: '',
        };
    },
    setup() {
        const alertStore = useAlertStore();
        const isAlertVisible = ref(false);
        const productStore = useProductStore();
        const auxSupliers = ref([]);
        const categories = ref([]);
        const products = ref([]);
        const supliers = ref([]);
        const selectedCategory = ref(null);
        const selectedSuplier = ref(null);
        const price = ref(null);
        const router = useRouter();


        const getCategory = async (url) => {
            try {
                const response = await axios.get(url);
                categories.value = response.data.results;
            } catch (error) {
                console.error('Error fetching categories', error);
            }
        };

        const getProduct = async (url) => {
            try {
                const response = await axios.get(url);
                products.value = response.data.results;
            } catch (error) {
                isAlertVisible.value = true;
                alertStore.showAlert('Erro ao buscar os produtos', 'error');
                console.error('Error fetching products', error);
            }
        };

        const getSuplier = async (url) => {
            try {
                const response = await axios.get(url);
                supliers.value = response.data.results;
            } catch (error) {
                isAlertVisible.value = true;
                alertStore.showAlert('Erro ao buscar os fornecedores', 'error');
                console.error('Error fetching supliers', error);
            }
        };

        const addProduct = async (productData) => {
            try {
                const response = await axios.post('/api/produtos/', productData);
                productStore.setProductData(productData);
                alertStore.showAlert('Fornecedor cadastrar com sucesso', 'success')
                productStore.resetFields();
                auxSupliers.value = [];

            } catch (error) {
                const errorMessage = error.response.data.name[0];
                alertStore.showAlert(`Erro ao cadastrar produto: ${errorMessage}`, 'error');
                console.error('Error adding product', error);
            }
        };

        const updateProduct = async (id, updateProduct) => {
            try {
                const response = await axios.put(`/api/produtos/${id}/`, updateProduct);
                productStore.setProductData(response.data);
                alertStore.showAlert('Fornecedor atualizado com sucesso', 'success');
                productStore.resetFields();
                router.replace('/product');
                return response
            } catch (error) {
                alertStore.showAlert('Erro ao cadastrar fornecedor.', 'error')
                console.error('Error adding suplier', error);
                throw error;
            }
        };

        const addAuxSuplierAndPrice = () => {
            const selectedSup = supliers.value.find((suplier) => suplier.id === selectedSuplier.value);
            const isExisting = auxSupliers.value.some(
                (auxSup) =>
                    auxSup.suplier === selectedSup.name || auxSup.suplier === selectedSup.name === ''
            );

            if (!selectedSup) {
                isAlertVisible.value = true;
                alertStore.showAlert('Fornecedor inválido', 'error');
            } else if (isExisting) {
                isAlertVisible.value = true;
                alertStore.showAlert('Fornecedor já adicionado', 'error');
            } else if (!price.value) {
                isAlertVisible.value = true;
                alertStore.showAlert('O campo de preço não pode estar vazio', 'error');
            } else {
                const parsedPrice = parseFloat(price.value.replace(',', '.'));
                if (isNaN(parsedPrice) || parsedPrice <= 0) {
                    isAlertVisible.value = true;
                    alertStore.showAlert('Formato de preço inválido', 'error');
                } else {
                    auxSupliers.value.push({
                        suplier: selectedSup.name,
                        price: parsedPrice,
                    });
                    isAlertVisible.value = true;
                    alertStore.showAlert('Fornecedor e Preço adicionados', 'success');
                }
            }

            selectedSuplier.value = null;
            price.value = '';
        };

        const removeAuxSuplierAndPrice = (index) => {
            if (index >= 0 && index < auxSupliers.value.length) {
                auxSupliers.value.splice(index, 1);
                alertStore.showAlert('Fornecedor removido da lista.', 'success');
            }
        };

        const submitForm = () => {
            const productData = {
                name: productStore.titleCase(productStore.productData.name),
                description: productStore.productData.description,
                category: productStore.productData.category.id,
                supliers: [...auxSupliers.value],
            };

            if (productStore.productData.editingProductId) {
                updateProduct(productStore.productData.editingProductId, productData);                
                productStore.resetFields();
            } else {
                addProduct(productData);
                productStore.resetFields();
            }
        };

        return {
            getCategory,
            getProduct,
            getSuplier,
            submitForm,
            removeAuxSuplierAndPrice,
            addAuxSuplierAndPrice,
            categories,
            products,
            supliers,
            selectedCategory,
            selectedSuplier,
            price,
            alertStore,
            isAlertVisible,
            productStore,
            productData: productStore.productData,
            auxSupliers,
            editingProductId: productStore.productData.editingProductId,
        };
    },

    computed: {
        selectedCategorySupliers() {
            const selectedProduct = this.products.find(product => product.id === this.selectedCategory);
            return selectedProduct ? selectedProduct.suplierproducts : [];
        },

    },
    components: {
        TheAlert,
    },
    mounted() {
        this.getCategory(this.baseURLCategory);
        this.getSuplier(this.baseURLSuplier);
        this.getProduct(this.baseURL);

        if (this.editingProductId) {
            this.auxSupliers = this.productStore.productData.supliers.map((suplier) => ({
                suplier: suplier.suplier,
                price: suplier.price,
            }));
        }
    },

    methods: {
        categoryChanged(event) {
            const categoryId = event.target.value;
            const selectedCategory = this.categories.find(
                (category) => category.id === parseInt(categoryId)
            );

            if (selectedCategory) {
                this.productStore.productData.category = selectedCategory;
            }
        },

    }
};
</script>


<style>
.plus {
    display: flex;
    padding-top: 30px;
}
</style>