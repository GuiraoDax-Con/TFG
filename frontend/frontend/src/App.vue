<script setup>
import NavbarModule from './components/modules/NavbarModule.vue';
import FooterModule from './components/modules/FooterModule.vue';
</script>

<template>
  <div>
    <NavbarModule />
    <router-view /> <!-- Aquí se renderizarán las rutas dinámicamente -->
    <FooterModule />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
