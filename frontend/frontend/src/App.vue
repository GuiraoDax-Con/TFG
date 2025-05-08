<template>
  <div id="app">
    <NavbarModule /> <!-- Navbar global -->
    <router-view /> <!-- Aquí se renderizarán tus componentes de ruta -->
  </div>
</template>

<script>
import NavbarModule from './components/modules/NavbarModule.vue';

export default {
  name: 'App',
  components: {
    NavbarModule,
  },
};
</script>

<style>
  @import './assets/css/AppStyle.css';
</style>
