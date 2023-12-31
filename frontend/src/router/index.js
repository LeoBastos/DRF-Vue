import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ProductView from '@/views/ProductView.vue'
import CategoryView from '@/views/CategoryView.vue'
import SuplierView from '@/views/SuplierView.vue'
import LoginView from '@/views/LoginView.vue'
import FormSuplier from '@/components/TheFormSuplier.vue'
import FormProduct from '@/components/TheFormProduct.vue'
import { useUserStore } from '@/stores/user'



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
      path: '/product/add',
      name: 'cadastro-produto',
      component: FormProduct
    },
    {
      path: '/category',
      name: 'categoria',      
      component: CategoryView
    },
    {
      path: '/suplier',
      name: 'fornecedores',      
      component: SuplierView,     
    },
    {
      path: '/suplier/add',
      name: 'cadastro-fornecedor',
      component: FormSuplier
    },
    {
      path: '/login',
      name: 'login',      
      component: LoginView
    }    
  ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()

  if (to.name !== 'login' && !userStore.user.isAuthenticated) {
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
