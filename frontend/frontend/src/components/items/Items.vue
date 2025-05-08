<template>
  <div class="items-page">
    <!-- Barra de búsqueda -->
    <div class="search-bar">
      <input
        type="text"
        v-model="searchQuery"
        placeholder="Buscar por nombre..."
        class="search-input"
      />
      <select v-model="filterType" class="filter-select">
        <option value="">Todos</option>
        <option value="arma">Arma</option>
        <option value="armadura">Armadura</option>
      </select>
      <button @click="fetchItems" class="search-button">Buscar</button>
    </div>

    <!-- Botón para mostrar el formulario de añadir ítem -->
    <button @click="showAddItemForm = true" class="add-item-button">
      Añadir Ítem
    </button>

    <!-- Formulario para añadir un nuevo ítem -->
    <div v-if="showAddItemForm" class="add-item-form">
      <h2>Añadir Nuevo Ítem</h2>
      <form @submit.prevent="addItem">
        <label>
          Nombre:
          <input type="text" v-model="newItem.Name" required />
        </label>
        <label>
          Precio:
          <input type="text" v-model="newItem.Price" required />
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
          <input type="text" v-model="newItem.AC" />
        </label>
        <label v-if="newItem.Type === 'arma'">
          Daño:
          <input type="text" v-model="newItem.Damage" />
        </label>
        <label>
          Peso:
          <input type="text" v-model="newItem.Weight" required />
        </label>
        <label>
          Propiedades:
          <input type="text" v-model="newItem.Properties" />
        </label>
        <button type="submit">Guardar</button>
        <button type="button" @click="resetForm">Cancelar</button>
      </form>
    </div>

    <!-- Lista de ítems -->
    <div class="items-list">
      <div v-for="item in filteredItems" :key="item.id" class="item-card">
        <h3>{{ item.Name }}</h3>
        <p>Precio: {{ item.Price }}</p>
        <p>Tipo: {{ item.Type }}</p>
        <p v-if="item.Type === 'armadura'">AC: {{ item.AC }}</p>
        <p v-if="item.Type === 'arma'">Daño: {{ item.Damage }}</p>
        <p>Peso: {{ item.Weight }}</p>
        <p>Propiedades: {{ item.Properties }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      items: [], // Lista de ítems
      searchQuery: "", // Filtro de búsqueda por nombre
      filterType: "", // Filtro por tipo (arma o armadura)
      showAddItemForm: false, // Controla la visibilidad del formulario
      newItem: {
        Name: "",
        Price: "",
        AC: "",
        Damage: "",
        Weight: "",
        Type: "",
        Properties: "",
      },
    };
  },
  computed: {
    filteredItems() {
      // Filtra los ítems según el nombre y el tipo
      return this.items.filter((item) => {
        const matchesName = item.Name.toLowerCase().includes(
          this.searchQuery.toLowerCase()
        );
        const matchesType =
          this.filterType === "" || item.Type.toLowerCase() === this.filterType;
        return matchesName && matchesType;
      });
    },
  },
  methods: {
    async fetchItems() {
      // Obtiene la lista de ítems desde el backend
      try {
        let response;
        if (this.searchQuery) {
          // Si hay un término de búsqueda, busca por nombre
          response = await axios.get(
            `http://127.0.0.1:8000/items/name/${this.searchQuery}`
          );
          this.items = [response.data]; // Asegúrate de que sea una lista
        } else {
          // Si no hay término de búsqueda, obtiene todos los ítems
          response = await axios.get("http://127.0.0.1:8000/items");
          this.items = response.data;
        }
      } catch (error) {
        console.error("Error al obtener los ítems:", error);
      }
    },
    async addItem() {
      // Envía el nuevo ítem al backend
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/items",
          this.newItem
        );
        this.items.push(response.data); // Añade el nuevo ítem a la lista
        this.resetForm(); // Resetea el formulario
      } catch (error) {
        console.error("Error al añadir el ítem:", error);
      }
    },
    resetForm() {
      // Resetea el formulario y oculta el modal
      this.showAddItemForm = false;
      this.newItem = {
        Name: "",
        Price: "",
        AC: "",
        Damage: "",
        Weight: "",
        Type: "",
        Properties: "",
      };
    },
  },
  mounted() {
    this.fetchItems(); // Carga los ítems al montar el componente
  },
};
</script>

<style scoped>
@import "../../assets/css/ItemsStyle.css";

</style>