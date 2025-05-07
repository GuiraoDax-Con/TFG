import { createRouter, createWebHistory } from 'vue-router'
import HomeComponent from '@/components/HomeComponent.vue';
import Items from "@/components/items/items.vue"; // Ruta correcta al componente

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
  // Puedes agregar más rutas aquí
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;