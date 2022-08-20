import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'
import Home from '../views/Home.vue'
import ProfileSetup from '../views/ProfileSetup.vue'
import About from '../views/About.vue'
import FindPet from '../views/FindPet.vue'
import FindGuardian from '../views/FindGuardian.vue'
import Pet from '../views/Pet.vue'
import Guardian from '../views/Guardian.vue'
import AddPet from '../views/AddPet.vue'
import EditPet from '../views/EditPet.vue'

import Settings from '../views/Settings.vue'
import MyAccount from '../views/MyAccount.vue'
import EditMyAccount from '../views/EditMyAccount.vue'

import SignUp from '../views/SignUp.vue'
import SignIn from '../views/SignIn.vue'
import ForgotPassword from '../views/ForgotPassword.vue'
import ForgotPasswordConfirmation from '../views/ForgotPasswordConfirmation.vue'
import UserActivation from '../views/UserActivation.vue'
import Help from '../views/Help.vue'
import MyPets from '../views/MyPets.vue'

const routes = [

  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn
  },
  {
    path: '/forgotpassword',
    name: 'ForgotPassword',
    component: ForgotPassword
  },
  {
    path: '/reset_password/:uid/:token',
    name: 'ForgotPasswordConfirmation',
    component: ForgotPasswordConfirmation
  },
  {
    path: '/activate/:uid/:token',
    name: 'UserActivation',
    component: UserActivation
  },
  {
    path: '/profilesetup',
    name: 'ProfileSetup',
    component: ProfileSetup,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    component: About
  },
  {
    path: '/findpet',
    name: 'FindPet',
    component: FindPet
  },
  {
    path: '/findpet/:house_slug',
    name: 'Pet',
    component: Pet,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/findguardian',
    name: 'FindGuardian',
    component: FindGuardian
  },
  

  {
    path: '/addpet',
    name: 'AddPet',
    component: AddPet,
    meta: {
      requireLogin: true
    }
  },

  {
    path: '/editpet/:house_slug',
    name: 'EditPet',
    component: EditPet,
    meta: {
      requireLogin: true
    }
  },

  

  {
    path: '/findguardian/:housemate_slug',
    name: 'Guardian',
    component: Guardian,
    meta: {
      requireLogin: true
    }
    
  },
  {
    path: '/settings',
    name: 'Settings',
    component: Settings
  },

  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    }
    
  },

  {
    path: '/myaccount/edit',
    name: 'EditMyAccount',
    component: EditMyAccount,
    meta: {
      requireLogin: true
    }
    
  },


  {
    path: '/help',
    name: 'Help',
    component: Help
  },
  
  {
    path: '/mypets',
    name: 'MyPets',
    component: MyPets,
    meta: {
      requireLogin: true
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior (to, from, savedPosition){
    return { top: 0 }
  },
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'SignIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
