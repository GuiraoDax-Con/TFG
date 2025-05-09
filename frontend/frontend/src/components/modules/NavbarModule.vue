<template>
  <nav class="nav-bar">
    
    <router-link to="/" class="logo-container-navbar">
      <img :src="logoSrc" alt="Logo de la página" />
    </router-link>
    <router-link to="/items" class="nav-item right">Items</router-link> <!-- Enlace a Items -->
    <router-link to="/calcular-xp" class="nav-item right">Calcular XP</router-link> <!-- Enlace a CalcularXP -->
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
  @import '@/assets/css/modulesStyle/NavbarStyle.css';
</style>