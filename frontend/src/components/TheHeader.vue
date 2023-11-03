<template>
    <header class="text-gray-600 body-font dark:bg-gray-700">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
            <nav class="md:ml-auto flex flex-wrap items-center text-base justify-center">
                <template v-if="userStore.user.isAuthenticated">
                    <RouterLink to="/" class="mr-5 hover:text-emerald-500 dark:text-white">Home</RouterLink>
                    <RouterLink to="/category" class="mr-5 hover:text-emerald-500 dark:text-white">Categorias</RouterLink>                   
                    <RouterLink to="/suplier" class="mr-5 hover:text-emerald-500 dark:text-white">Fornecedores</RouterLink>
                    <RouterLink to="/product" class="mr-5 hover:text-emerald-500 dark:text-white">Produtos</RouterLink>
                    <a href="#" class="mr-5 hover:text-emerald-500 dark:text-white" @click="logout">Logout</a>
                </template>
                <template v-else>
                    <RouterLink to="/" class="mr-5 hover:text-emerald-500 dark:text-white">Login</RouterLink>
                </template>
            </nav>
        </div>
    </header>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },

    components: {

    },

    beforeCreate() {
        this.userStore.initStore()
        const token = this.userStore.user.access

        if (token) {
            axios.defaults.headers.common["Authorization"] = "Bearer " + token;
        } else {
            axios.defaults.headers.common["Authorization"] = "";
        }
    },
    methods: {
        logout() {
            this.userStore.removeToken()
            this.$router.push('/login')
        }

    }
}
</script>

    


