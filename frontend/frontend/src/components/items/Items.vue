<template>
  <div class="body-page">
    
    <h1>Items</h1>

    <!-- Barra de búsqueda -->
    <div class="filtros-busqueda">
        <div class="barra-busqueda">
          <input
            type="text"
            v-model="searchQuery"
            placeholder="Buscar item por nombre..."
            class="barra-busqueda-input"
          />
          
        </div>
        <div class="filtro">
          <label for="tipo">Tipo:</label>
          <select id="tipo" v-model="filterType">
            <option value="">Todos</option>
            <option value="arma">Arma</option>
            <option value="armadura">Armadura</option>
          </select>
        </div>
    </div>
    

    <!-- Botón para añadir ítems -->
    <div class="add-item-container">
      <button @click="addItem" class="btn-añadir">Añadir Ítem</button>
    </div>

    <!-- Tabla de ítems -->
    <table>
      <thead>
        <tr class="primary-color">
          <th>Id</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Tipo</th>
          <th>AC/Daño</th>
          <th>Peso</th>
          <th>Propiedades</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.id">
          <td>{{ item.id }}</td>
          <td>{{ item.Name }}</td>
          <td>{{ item.Price }}</td>
          <td>{{ item.Type }}</td>
          <td>{{ item.Type === 'armadura' ? item.AC : item.Damage }}</td>
          <td>{{ item.Weight }}</td>
          <td>{{ item.Properties }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import itemsAPI from '../../services/itemsAPI';

export default {
  data() {
    return {
      items: [], // Lista de ítems
      searchQuery: "", // Filtro de búsqueda por nombre
      filterType: "", // Filtro por tipo (arma o armadura)
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
    addItem() {
      console.log("Ir a Añadir ítem");
      this.$router.push("/add-item");
    },
    async fetchItems() {
      // Obtiene la lista de ítems desde el backend usando itemsAPI
      try {
        this.items = await itemsAPI.getItems();
      } catch (error) {
        console.error("Error al obtener los ítems:", error);
      }
    }, 
  },
  mounted() {
    this.fetchItems(); // Carga los ítems al montar el componente
  },
};
</script>

<style scoped>
  @import "../../assets/css/ItemsStyles/ItemsStyle.css";
</style>