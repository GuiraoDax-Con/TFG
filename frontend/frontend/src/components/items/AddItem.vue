<template>
  <div class="add-page">

    <br>
    <h1>Añadir Nuevo Ítem</h1>

    <form @submit.prevent="addItem">
      <div class="form-group">
        <label>Nombre:</label>
        <input type="text" v-model="newItem.Name" required />
      </div>

      <div class="form-group">
        <label>Precio:</label>
        <input type="text" v-model="newItem.Price" required
          @input="validateNumberInput('Price')"
          placeholder="Num"
        />
      </div>
      
      <div class="form-group">
          <label>Tipo:</label>
          <select v-model="newItem.Type" required>
            <option value="arma">Arma</option>
            <option value="armadura">Armadura</option>
          </select>
      </div>

      <div class="form-group">
          <label v-if="newItem.Type === 'armadura'">AC:</label>
          <input v-if="newItem.Type === 'armadura'"
            type="text" v-model="newItem.AC"
            @input="validateNumberInput('AC')"
            placeholder="num"
          />
      </div>

      <div class="form-group">
        <label v-if="newItem.Type === 'arma'">Daño:</label>
        <input v-if="newItem.Type === 'arma'" 
          type="text" v-model="newItem.Damage" />
      </div>

      <div class="form-group">
          <label>Peso:</label>
          <input type="text" v-model="newItem.Weight" required
            @input="validateNumberInput('Weight')"
            placeholder="num"
          />
      </div>

      <div class="form-group">
          <label>Propiedades:</label>
          <input type="text" v-model="newItem.Properties" />
      </div>

      <div class="form-group">
          <label>URL de imagen (opcional):</label>
          <input type="text" v-model="newItem.img" placeholder="https://..." />
      </div>

      <div class="form-group"></div>

      <Toast ref="toast" />
      
      <button type="submit">Guardar</button>
      <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script>
  import itemsAPI from "@/services/itemsAPI";
  import Toast from "../modules/Toast.vue";

  export default {
    components: {
      Toast,
    },
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
          img: "", // Campo opcional para la URL de la imagen
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
          // Usa el servicio para crear el ítem
          await itemsAPI.createItem(this.newItem);
          console.log("Ítem añadido con éxito");

          // Reinicia el formulario después de guardar
          this.newItem = {
            Name: "",
            Price: "",
            AC: "",
            Damage: "",
            Weight: "",
            Type: "",
            Properties: "",
            img: "",
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
  @import "@/assets/css/addPageStyle.css";
</style>
