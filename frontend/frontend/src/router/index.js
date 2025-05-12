import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '@/components/HomeComponent.vue';
import Items from "@/components/items/items.vue";
import AddItem from "@/components/add/AddItem.vue"; 
import CalcularXP from '@/components/Calculadora/CalcularXP.vue'; 
import Dice from '@/components/dice/dice.vue'; 

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeComponent,
  },

  {
    path: "/items",
    name: "Items",
    component: Items,
  },

  {
    path: "/add-item",
    name: "AddItem",
    component: AddItem,
  },

  {
    path: '/calcular-xp',
    name: 'CalcularXP',
    component: CalcularXP,
  },
  {
    path: '/dice',
    name: 'Dice',
    component: Dice,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;