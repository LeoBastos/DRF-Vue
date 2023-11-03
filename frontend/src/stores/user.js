import { defineStore } from 'pinia'
import axios from 'axios'

export const useUserStore = defineStore({
    id: 'user',

    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            name: null,
            email: null,
            access: null,
            refresh: null,            
        }
    }),

    actions: {
        initStore() {
            if (sessionStorage.getItem('user.access')) {
                this.user.access = sessionStorage.getItem('user.access')
                this.user.refresh = sessionStorage.getItem('user.refresh')
                this.user.id = sessionStorage.getItem('user.id')
                this.user.name = sessionStorage.getItem('user.name')
                this.user.email = sessionStorage.getItem('user.email')               
                this.user.isAuthenticated = true

                this.refreshToken()
            }
        },

        setToken(data) {
            this.user.access = data.access
            this.user.refresh = data.refresh
            this.user.isAuthenticated = true

            sessionStorage.setItem('user.access', data.access)
            sessionStorage.setItem('user.refresh', data.refresh)
        },

        removeToken() {
            this.user.refresh = null
            this.user.access = null
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.name = null
            this.user.email = null

            sessionStorage.setItem('user.access', '')
            sessionStorage.setItem('user.refresh', '')
            sessionStorage.setItem('user.id', '')
            sessionStorage.setItem('user.name', '')
            sessionStorage.setItem('user.email', '')
           
        },
      

        refreshToken() {
            axios.post('/api/token/refresh/', {
                refresh: this.user.refresh
            })
                .then((response) => {
                    this.user.access = response.data.access

                    sessionStorage.setItem('user.access', response.data.access)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
                })
                .catch((error)=>{
                    console.log(error)

                    this.removeToken()
                })
        },
    }
})