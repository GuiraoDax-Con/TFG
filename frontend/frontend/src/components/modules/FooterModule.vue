// src/components/modules/FooterModule.vue
<template>
  <footer class="footer">
    <div class="footer-content">
      <div class="footer-top">
        <p>Síguenos en nuestras redes sociales:</p>
        <div class="social-icons">
          <a href="https://www.facebook.com/" target="_blank" aria-label="Facebook">
            <font-awesome-icon :icon="['fab', 'facebook-f']" />
          </a>
          <a href="https://twitter.com/" target="_blank" aria-label="Twitter">
            <font-awesome-icon :icon="['fab', 'twitter']" />
          </a>
          <a href="https://www.instagram.com/" target="_blank" aria-label="Instagram">
            <font-awesome-icon :icon="['fab', 'instagram']" />
          </a>
        </div>
      </div>

      <nav class="footer-nav">
        <ul>
          <li><a href="/about">Acerca de</a></li>
          <li><a href="/contact">Contacto</a></li>
          <li><a href="/privacy">Política de Privacidad</a></li>
        </ul>
      </nav>

      <div class="footer-bottom">
        <p>© {{ year }} La Guarida del Dungeon Master. Todos los derechos reservados.</p>
      </div>
       <div class="footer-left">
            <a href="https://moodle.iescierva.net/" target="_blank" aria-label="IES Ingeniero de la Cierva">
              <img
                src="https://moodle.iescierva.net/pluginfile.php/1/theme_adaptable/adaptablemarkettingimages/0/logoIES_280x80.jpg"
                alt="IES Ingeniero de la Cierva"
                class="ies-logo"
              />
            </a>
        </div>
    </div>
  </footer>
</template>

<script>
  import { library } from '@fortawesome/fontawesome-svg-core';
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
  import { faFacebookF, faTwitter, faInstagram } from '@fortawesome/free-brands-svg-icons';

  library.add(faFacebookF, faTwitter, faInstagram);

  export default {
    name: 'FooterModule',
    components: {
      'font-awesome-icon': FontAwesomeIcon,
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