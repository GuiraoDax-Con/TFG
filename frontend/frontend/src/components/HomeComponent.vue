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
        <button class="button primary-color tienda-button" @click="goToTienda">Tienda</button>
        <button class="button primary-color calcular-xp-button" @click="calcularXP">Calcular XP</button>
      </div>

      <!-- Componente Toast agregado aquí -->
      <Toast ref="toast" />
    </main>
  </div>
</template>
  
<script>
  import logo from '@/assets/images/logo.png'; // Importa la imagen
  import Toast from './modules/Toast.vue'; // Importa el componente Toast

  export default {
    name: 'HomePage',
    components: { Toast }, // Importart Toast en el componentes
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
          this.$router.push('/calcular-xp');
        }, 1000);
      },
      calcularXP() {
        console.log('Calcular XP');
        this.$refs.toast.show('Calcular XP'); // Usar Toast en vez de alert

        setTimeout(() => {
          this.$router.push('/calcular-xp');
        }, 1000);
      },
    },
  };
</script>

<style scoped>
    @import '../assets/css/HomeStyle.css';
</style>