<template>
  <TheHeader />
  <main>
    <RouterView />
  </main>
</template>


<script>
    import axios from 'axios'
    import TheHeader from '@/components/TheHeader.vue';
    import { useUserStore } from '@/stores/user'

    export default {
        setup() {
            const userStore = useUserStore()

            return {
                userStore
            }
        },

        components: {
          TheHeader
        },

        beforeCreate() {
            this.userStore.initStore()

            const token = this.userStore.user.access

            if (token) {
                axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            } else {
                axios.defaults.headers.common["Authorization"] = "";
            }
        }

        
    }
</script>