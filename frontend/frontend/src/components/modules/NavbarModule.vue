<template>
  <nav class="nav-bar">
    <div class="nav-item left">Izquierda</div>
    <router-link to="/" class="logo-container-navbar">
      <img :src="logoSrc" alt="Logo de la página" />
    </router-link>
    <div class="nav-item right">Derecha</div>
  </nav>
</template>
  
<script>
  import logo from '@/assets/images/logo.png';
  
  export default {
    name: 'NavBar',
    data() {
      return {
        logoSrc: logo
      };
    },
  };
</script>

<style scoped>
  @import '../../assets/css/NavbarStyle.css';
</style>