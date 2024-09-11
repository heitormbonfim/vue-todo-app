import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/AboutView.vue')
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('@/views/Settings.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/SignupView.vue'),
      meta: {
        requiresAuth: false
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/LoginView.vue')
    },
    {
      path: '/:catchAll(.*)',
      name: 'not-found',
      component: () => import('@/views/NotFound.vue'),
      meta: {
        requiresAuth: false
      }
    }
  ]
})

router.beforeEach((to, _from, next) => {
  const auth = true

  if (to.name === 'login') {
    next() // login route is always  okay (we could use the requires auth flag below). prevent a redirect loop
  } else if (to.meta && to.meta.requiresAuth === false) {
    next() // requires auth is explicitly set to false
  } else if (auth) {
    next() // i'm logged in. carry on
  } else {
    next({ name: 'login' }) // always put your redirect as the default case
  }
})

export default router
