import { createApp } from 'vue';
import App from './App.vue';
import router from './router'; // Importa el enrutador

const app = createApp(App);

app.use(router); // Usa el enrutador
app.mount('#app');
