<template>
  <div class="add-item-page">
    <div class="image-container">
      <img src="@/assets/images/addItems_img.png" alt="" class="centered-image" />
    </div>
    <h1>Añadir Nuevo Ítem</h1>
    <form @submit.prevent="addItem">
      <label>
        Nombre:
        <input type="text" v-model="newItem.Name" required />
      </label>
      <label>
        Precio:
        <input
          type="text"
          v-model="newItem.Price"
          @input="validateNumberInput('Price')"
          placeholder="num"
          required
        />
      </label>
      <label>
        Tipo:
        <select v-model="newItem.Type" required>
          <option value="arma">Arma</option>
          <option value="armadura">Armadura</option>
        </select>
      </label>
      <label v-if="newItem.Type === 'armadura'">
        AC:
        <input
          type="text"
          v-model="newItem.AC"
          @input="validateNumberInput('AC')"
          placeholder="num"
        />
      </label>
      <label v-if="newItem.Type === 'arma'">
        Daño:
        <input type="text" v-model="newItem.Damage" />
      </label>
      <label>
        Peso:
        <input
          type="text"
          v-model="newItem.Weight"
          required
          @input="validateNumberInput('Weight')"
          placeholder="num"
        />
      </label>
      <label>
        Propiedades:
        <input type="text" v-model="newItem.Properties" />
      </label>
      <button type="submit">Guardar</button>
    </form>
    <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      newItem: {
        Name: "",
        Price: "",
        AC: "",
        Damage: "",
        Weight: "",
        Type: "",
        Properties: "",
      },
      errorMessage: "", // Mensaje de error
    };
  },
  methods: {
    validateNumberInput(field) {
      // Permite solo números en el campo especificado
      this.newItem[field] = this.newItem[field].replace(/[^0-9]/g, "");
    },
    async addItem() {
      try {
        // Realiza una solicitud POST al backend
        const response = await axios.post("http://127.0.0.1:8000/items", this.newItem);
        console.log("Ítem añadido con éxito:", response.data);

        // Reinicia el formulario después de guardar
        this.newItem = {
          Name: "",
          Price: "",
          AC: "",
          Damage: "",
          Weight: "",
          Type: "",
          Properties: "",
        };

        // Limpia el mensaje de error si la solicitud fue exitosa
        this.errorMessage = "";

        // Opcional: Redirige a la página de ítems
        this.$router.push("/items");
      } catch (error) {
        console.error("Error al añadir el ítem:", error);
        // Muestra un mensaje de error al usuario
        this.errorMessage = "No se pudo crear el ítem. Por favor, verifica los datos e inténtalo de nuevo.";
      }
    },
  },
};
</script>

<style scoped>
@import '../../assets/css/AddItemsStyle.css';


</style>
