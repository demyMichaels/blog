import Vue from 'vue';
import Router from 'vue-router';
import Placeholder from '../views/Placeholder.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Placeholder // Use Placeholder component as a temporary home
    }
    // Add more routes here as your application grows
  ]
});
