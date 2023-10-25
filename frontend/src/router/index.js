import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProductView from '../views/ProductView.vue'
import CategoryView from '../views/CategoryView.vue'
import SuplierView from '../views/SuplierView.vue'
import LoginView from '../views/LoginView.vue'



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/product',
      name: 'produtos',      
      component: ProductView
    },
    {
      path: '/category',
      name: 'categoria',      
      component: CategoryView
    },
    {
      path: '/suplier',
      name: 'fornecedores',      
      component: SuplierView
    },
    {
      path: '/login',
      name: 'login',      
      component: LoginView
    }    
  ]
})

export default router
