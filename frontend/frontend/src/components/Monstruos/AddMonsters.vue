<template>
  <div class="add-monster-container">
    <div class="logo-container">
      <img src="@/assets/images/calculadora-xp_imagenes/addMonster.png" alt="Añadir Monstruo" class="add-monster-logo" />
    </div>
    
    <h2>Añadir Nuevo Monstruo</h2>

    <form @submit.prevent="guardarMonstruo">
      <div class="form-group">
        <label>Nombre:</label>
        <input v-model="monster.name" type="text" required />
      </div>

      <div class="form-group">
        <label>Tamaño:</label>
        <select v-model="monster.size" required>
          <option value="" disabled hidden>Seleccione...</option>
          <option value="Diminuto">Diminuto</option>
          <option value="Pequeño">Pequeño</option>
          <option value="Mediano">Mediano</option>
          <option value="Grande">Grande</option>
          <option value="Enorme">Enorme</option>
          <option value="Colosal">Colosal</option>
        </select>
      </div>

      <div class="form-group">
        <label>Tipo:</label>
        <select v-model="monster.type" required>
          <option value="" disabled hidden>Seleccione...</option>
          <option value="Aberración">Aberración</option>
          <option value="Bestia">Bestia</option>
          <option value="Celestial">Celestial</option>
          <option value="Constructo">Constructo</option>
          <option value="Dragón">Dragón</option>
          <option value="Elemental">Elemental</option>
          <option value="Hada">Hada</option>
          <option value="Demonio">Demonio</option>
          <option value="Gigante">Gigante</option>
          <option value="Humanoide">Humanoide</option>
          <option value="Monstruosidad">Monstruosidad</option>
          <option value="Moco">Moco</option>
          <option value="Planta">Planta</option>
          <option value="No muerto">No muerto</option>
        </select>
      </div>

      <div class="form-group">
        <label>Raza (Tag):</label>
        <input v-model="monster.tag" type="text" />
      </div>

      <div class="form-group">
        <label>Alineamiento:</label>
        <select v-model="monster.alignment">
          <option value="" disabled hidden>Seleccione...</option>
          <option value="Legal Bueno">Legal Bueno</option>
          <option value="Neutral Bueno">Neutral Bueno</option>
          <option value="Caótico Bueno">Caótico Bueno</option>
          <option value="Legal Neutral">Legal Neutral</option>
          <option value="Neutral Verdadero">Neutral Verdadero</option>
          <option value="Caótico Neutral">Caótico Neutral</option>
          <option value="Legal Malvado">Legal Malvado</option>
          <option value="Neutral Malvado">Neutral Malvado</option>
          <option value="Caótico Malvado">Caótico Malvado</option>
          <option value="Sin alineamiento">Sin alineamiento</option>
        </select>
      </div>

      <div class="form-group">
        <label>CR:</label>
        <select v-model="monster.cr" required>
          <option value="" disabled hidden>Seleccione...</option>
          <option v-for="cr in crOptions" :key="cr" :value="cr">{{ cr }}</option>
        </select>
      </div>

      <div class="form-group">
        <label>Libro Origen:</label>
        <input v-model="monster.sourceBook" type="text" />
      </div>

      <img class="monster-img-preview" v-if="monster.img" :src="monster.img" alt="Imagen del monstruo" />

      <div class="form-group">
        <label>Imagen (JPG o PNG):</label>
        <input type="file" accept="image/png, image/jpeg" @change="handleImageUpload" />
      </div>

      <button type="submit">Guardar</button>
      <p class="error-msg" v-if="error">{{ error }}</p>
      <p class="success-msg" v-if="exito">{{ exito }}</p>
    </form>

  </div>
</template>

<script setup>
  import { ref } from 'vue';
  import monsterAPI from "@/services/monstersAPI.js";

  const monster = ref({
    name: "",
    size: "",
    type: "",
    tag: "",
    alignment: "",
    cr: "",
    sourceBook: "",
    img: ""
  });

  const error = ref("");
  const exito = ref("");

  const crOptions = [
    "0", "1/8", "1/4", "1/2", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"
  ];


  const handleImageUpload = (event) => {
    const file = event.target.files[0];
    if (file && (file.type === "image/png" || file.type === "image/jpeg")) {
      const reader = new FileReader();
      reader.onload = () => {
        monster.value.img = reader.result;
      };
      reader.readAsDataURL(file);
    } else {
      error.value = "Formato de imagen inválido. Solo se permite PNG o JPG.";
    }
  };

  const guardarMonstruo = async () => {
    error.value = "";
    exito.value = "";

    if (!monster.value.name || !monster.value.size || !monster.value.type || !monster.value.cr) {
      error.value = "Por favor completa todos los campos obligatorios.";
      return;
    }

    try {
      await monsterAPI.createMonster({ ...monster.value });
      exito.value = "Monstruo creado correctamente.";
      Object.keys(monster.value).forEach(key => monster.value[key] = "");
    } catch (err) {
      error.value = "No se pudo crear el monstruo. Verifica los datos e inténtalo de nuevo.";
    }
  };
</script>

<style scoped>
    @import "@/assets/css/MonstersStyles/AddMonsterStyle.css";
</style>
