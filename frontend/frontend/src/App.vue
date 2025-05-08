<template>
  <div id="app">
    <router-view /> <!- Aquí se renderizarán tus componentes de ruta -->
  </div>
</template>

<script>
  export default {
    name: 'App',
  };
</script>

<style>
  @import './assets/css/AppStyle.css';
</style>
