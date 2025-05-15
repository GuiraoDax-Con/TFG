import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Importa el router
import './assets/css/AppStyle.css'
import './assets/css/TableStyle.css';
import './assets/css/FiltrosStyle.css';

const app = createApp(App);
app.use(router); // Usa el router
app.mount('#app');