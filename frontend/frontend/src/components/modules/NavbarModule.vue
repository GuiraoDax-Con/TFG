<template>
  <nav class="nav-bar">
    
    <router-link to="/" class="logo-container-navbar left" title="Pagina de Inicio">
      <img :src="logoSrc" alt="Logo de la página" />
    </router-link>
    <router-link to="/items" class="nav-item left">Items</router-link> <!-- Enlace a Items -->
    <router-link to="/calcular-xp" class="nav-item left">Calcular XP</router-link> <!-- Enlace a CalcularXP -->
    <router-link to="/dice" class="tirar-dado-enlace nav-item rigth">Tirar Dado</router-link> <!-- Enlace a Añadir Ítem -->
  </nav>
</template>
  
<script>
  import logo from '@/assets/images/favicon.png';
  
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