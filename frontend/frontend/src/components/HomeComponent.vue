//HomeComponent.vue
<template>
  <div class="home-page">
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
  </div>
</template>
  

<script> 
  import logo from '@/assets/images/favicon.png'; // Importa la imagen
  import Toast from './modules/Toast.vue'; // Importa el componente Toast


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

        this.$refs.toast.show('Ir a la tienda'); // Usar Toast en vez de alert
        
        setTimeout(() => {
          this.$router.push('/items');
        }, 1000);
      },
      calcularXP() {
        console.log('Calcular XP');
        
        this.$refs.toast.show('Ir al bestiario'); // Usar Toast en vez de alert

        this.$router.push('/calcular-xp');
      },
    },
  };
</script>

<style scoped>
    @import '../assets/css/HomeStyle.css';
</style>