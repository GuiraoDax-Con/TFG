import { createApp } from 'vue'
import './style.css'
import router  from './router'
import App from './App.vue'

//createApp(App).mount('#app')

const app = createApp(App);

app.use(router); // Usa el enrutador
app.mount('#app');
