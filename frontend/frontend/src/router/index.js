import { createRouter, createWebHistory } from 'vue-router';
import HomeComponent from '@/components/HomeComponent.vue';
import Items from "@/components/items/Items.vue";
import AddItem from "@/components/items/AddItem.vue"; 
import CalcularXP from '@/components/Monstruos/CalcularXP.vue'; 
import AddMonsters from '@/components/Monstruos/AddMonsters.vue';
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
    path: '/add-monster',
    name: 'AddMonsters',
    component: AddMonsters,
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