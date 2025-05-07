// src/components/modules/MessageSystem.vue
<template>
  <div class="message-system" :class="positionClass">
    <transition-group name="message-transition" tag="div">
      <div
        v-for="message in messages"
        :key="message.id"
        class="message"
        :class="[message.type, message.customClass]"
      >
        <div class="message-content">
          <p v-if="message.title" class="message-title">{{ message.title }}</p>
          <p class="message-text">{{ message.text }}</p>
        </div>
        <button
          v-if="message.showClose"
          class="message-close"
          @click="removeMessage(message.id)"
        >
          &times;
        </button>
      </div>
    </transition-group>
  </div>
</template>

<script>
import { v4 as uuidv4 } from 'uuid';

export default {
  name: 'MessageSystem',
  data() {
    return {
      messages: [],
      position: 'top-right', // Puedes cambiar la posición por defecto
    };
  },
  computed: {
    positionClass() {
      // Devuelve la clase CSS correspondiente a la posición
      return `message-position-${this.position}`;
    },
  },
  methods: {
    showMessage(options) {
      // Muestra un nuevo mensaje
      const id = uuidv4();
      const defaultOptions = {
        id,
        type: 'info',
        title: '',
        text: '',
        duration: 5000, // 5 segundos por defecto
        showClose: true,
        customClass: '', // Permite añadir clases CSS personalizadas
        onClose: null, // Función a ejecutar al cerrar el mensaje
      };
      const message = { ...defaultOptions, ...options };
      this.messages.push(message);

      if (message.duration > 0) {
        setTimeout(() => {
          this.removeMessage(id);
        }, message.duration);
      }
      return id; // Devuelve el ID del mensaje para control manual
    },
    removeMessage(id) {
      // Elimina un mensaje por su ID
      const index = this.messages.findIndex((m) => m.id === id);
      if (index !== -1) {
        const message = this.messages[index];
        this.messages.splice(index, 1);
        if (message.onClose) {
          message.onClose();
        }
      }
    },
    // Métodos abreviados para diferentes tipos de mensajes
    info(text, title = '', options = {}) {
      return this.showMessage({ ...options, type: 'info', text, title });
    },
    success(text, title = '', options = {}) {
      return this.showMessage({ ...options, type: 'success', text, title });
    },
    warning(text, title = '', options = {}) {
      return this.showMessage({ ...options, type: 'warning', text, title });
    },
    error(text, title = '', options = {}) {
      return this.showMessage({ ...options, type: 'error', text, title });
    },
  },
};
</script>

<style scoped>
    @import '../../assets/css/MessageSystemStyle.css';
</style>
