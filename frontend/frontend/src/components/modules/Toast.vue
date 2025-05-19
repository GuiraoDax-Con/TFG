<template>
  <transition name="fade">
    <div v-if="visible" class="toast">
      {{ message }}
    </div>
  </transition>
</template>

<script>
export default {
  data() {
    return {
      visible: false,
      message: ''
    };
  },
  methods: {
    show(msg, duration = 3000) {
      this.message = msg;
      this.visible = true;
      setTimeout(() => {
        this.visible = false;
      }, duration);
    }
  }
};
</script>

<style scoped>
  .toast {
    position: fixed;
    bottom: 20px;
    left: center;
    right: center;
    background-color: #05619a;
    color: white;
    padding: 12px 20px;
    border-radius: 5px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.3);
    font-weight: bold;
    z-index: 9999;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
</style>
