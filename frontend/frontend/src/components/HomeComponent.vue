//HomeComponent.vue
<template>
  <div class="home-page">
    <main class="main-content">
      <div class="logo-container-home">
        <img :src="logoSrc" alt="Logo de la Guarida del Dungeon Master" class="main-logo-home" />
        
        <h1 class="logo-text">
          Bienvenido a la
          <br>
          Guarida del 
          <br>
          Dungeon Master
        </h1>
      </div>

      <div class="buttons-container">
        <button class="button tienda-button" @click="goToTienda">Tienda</button>
        <button class="button calcular-xp-button" @click="calcularXP">Calcular XP</button>
      </div>
    </main>
  </div>
</template>
  
<script>
  import logo from '@/assets/images/logo.png'; // Importa la imagen

  export default {
    name: 'HomePage',
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
        //alert('Ir a la tienda');
        // Aquí iría la lógica para calcular la XP
        // Por ejemplo, podrías redirigir a otra página o abrir un modal
        this.$router.push('/items');
      },
      calcularXP() {
        console.log('Calcular XP');
        alert('Calcular XP');
        //alert('Calcular XP');
        // Aquí iría la lógica para calcular la XP
        // Por ejemplo, podrías redirigir a otra página o abrir un modal
        this.$router.push('/calcular-xp');
      },
    },
  };
</script>

<style scoped>
    @import '../assets/css/HomeStyle.css';
</style>