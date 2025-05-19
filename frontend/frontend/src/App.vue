<template>
  <div id="app">
    <NavbarModule /> <!-- Navbar global -->
    <router-view /> <!-- Aquí se renderizarán tus componentes de ruta -->
    <FooterModule /> <!-- Footer global -->
  </div>
</template>

<script>
import NavbarModule from './components/modules/NavbarModule.vue';
import FooterModule from './components/modules/FooterModule.vue';

export default {
  name: 'App',
  components: {
    NavbarModule,
    FooterModule,
  },
};
</script>

<style>
</style>
