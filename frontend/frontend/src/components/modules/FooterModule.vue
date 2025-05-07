// src/components/modules/FooterModule.vue
<template>
  <footer class="footer">
    <div class="footer-content">
      <p>Síguenos en nuestras redes sociales:</p>
      <div class="social-icons">
        <a href="#" aria-label="Facebook"><font-awesome-icon :icon="['fab', 'facebook-f']" /></a>
        <a href="#" aria-label="Twitter"><font-awesome-icon :icon="['fab', 'twitter']" /></a>
        <a href="#" aria-label="Instagram"><font-awesome-icon :icon="['fab', 'instagram']" /></a>
      </div>
      <p>© {{ year }} La Guarida del Dungeon Master. Todos los derechos reservados.</p>
    </div>
  </footer>
</template>

<script>
    import { library } from '@fortawesome/fontawesome-svg-core';
    import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
    import { faFacebookF, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';

    library.add(faFacebookF, faTwitter, faInstagram);

    // Lo nuestro
    ///import logo from '@/assets/images/logo.png';
    ///import IES_Cierva_logo from '@/assets/images/favicon_ies-cierva.ico'; // Ruta de la imagen del logo del IES Cierva


    export default {
        name: 'FooterModule', // Cambiado a 'FooterModule'
        components: {
            'font-awesome-icon': FontAwesomeIcon, // Registrado con un nombre válido
        },
        data() {
            return {
                year: new Date().getFullYear(),
            };
        },
    };
</script>

<style scoped>
    @import '@/assets/css/modulesStyle/FooterStyle.css';
</style>