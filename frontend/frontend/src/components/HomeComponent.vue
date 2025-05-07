<template>
  <div class="home-page">
    <Navbar />

    <main class="main-content">
      <div class="logo-container-home">
        <img :src="logoSrc" alt="Logo de la Guarida del Dungeon Master" class="main-logo-home" />
        
        <h1 class="logo-text">
          Bienvenido a la
          <br>
          Guarida del Dungeon
          <br>
          Master
        </h1>
      </div>

      <div class="buttons-container">
        <button class="button tienda-button" @click="goToTienda">Tienda</button>
        <button class="button calcular-xp-button" @click="calcularXP">Calcular XP</button>
      </div>
    </main>
    
    <FooterModule />
  </div>
</template>
  
<script>
  import logo from '@/assets/images/logo.png'; // Importa la imagen
  import Navbar from "@/components/modules/NavbarModule.vue"; // Importa el componente Navbar
  import FooterModule from "@/components/modules/FooterModule.vue"; // Importa el componente Footer

  export default {
    name: 'HomePage',
    components: {
      Navbar,
      FooterModule, // Registra el componente Footer
    },
    data() {
      return {
        logoSrc: logo // Asigna la ruta importada a la propiedad data
      };
    },
    methods: {
      goToTienda() {
        console.log('Ir a la tienda');
        alert('Ir a la tienda');
        // Aquí iría la lógica para navegar a la tienda
      },
      calcularXP() {
        console.log('Calcular XP');
        alert('Calcular XP');
        // Aquí iría la lógica para calcular la XP
      },
    },
  };
</script>

<style scoped>
    @import '../assets/css/HomeStyle.css';
</style>