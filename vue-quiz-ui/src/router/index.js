import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import NonValidUsername from '../views/NonValidUsername.vue'
import QuestionsManager from '../views/QuestionsManager.vue'
import QuizFini from '../views/QuizFini.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'homePage',
      component: HomePage
    },
    // {
    //   path: '/*',
    //   redirect: '/'
    // },
    {
      path: '/newQuizPage',
      name: 'newQuizPage',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/NewQuizPage.vue')
    },
    {
      path:'/questions',
      name: 'questions',
      component: QuestionsManager
    },
    {
      path:'/nonValidUsername',
      name: 'NonValidUsername',
      component: NonValidUsername
    },
    {
      path:'/quizFini',
      name:'QuizFini',
      component: QuizFini
    }
  ]
})
export default router
