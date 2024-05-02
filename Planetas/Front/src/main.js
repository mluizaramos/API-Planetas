import { createApp } from 'vue'; // Importe createApp em vez de Vue
import App from './App.vue';
import router from './router/router';

createApp(App).use(router).mount('#app'); // Use createApp para criar a instância do aplicativo e use o Vue Router
