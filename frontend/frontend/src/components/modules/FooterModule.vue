<template>
    <footer class="footer-bar">
        <div class="footer-content">
        <div class="footer-item">
            <img :src="ciervaLogoSrc" alt="Logo de la página" class="footer-logo" />
            <h3>Ingeniro de la cierva</h3>
        </div>
        
        <div class="footer-item">Derecha</div>
        </div>
    </footer>
</template>

<script>
    import logo from '@/assets/images/logo.png';
    import IES_Cierva_logo from '@/assets/images/favicon_ies-cierva.ico'; // Ruta de la imagen del logo del IES Cierva
    import { defineComponent } from 'vue';

    export default {
        name: 'FooterModule',
        data() {
            return {
                year: new Date().getFullYear(),
            };
        },
    };
</script>

<style scoped>
    @import '../../assets/css/FooterStyle.css';
</style>