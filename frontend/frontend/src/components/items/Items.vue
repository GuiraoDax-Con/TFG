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
          <th>Imagen</th>
          <th>Nombre</th>
          <th>Precio</th>
          <th>Tipo</th>
          <th>AC/Daño</th>
          <th>Peso</th>
          <th>Propiedades</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in filteredItems" :key="item.id" class="item-row">
          <td>
            <img v-if="item.img && editId !== item.id" :src="item.img" alt="Imagen" style="max-width: 50px; max-height: 50px;" />
            <!-- Input para editar la URL de la imagen -->
            <input
              v-if="editId === item.id"
              v-model="editItem.img"
              type="text"
              placeholder="URL de la imagen"
              style="max-width: 120px;"
            />
          </td>
          <td v-if="editId !== item.id">{{ item.Name }}</td>
          <td v-else><input v-model="editItem.Name" /></td>

          <td v-if="editId !== item.id">{{ item.Price }}</td>
          <td v-else>
            <input v-model.number="editItem.Price" type="number" min="0" />
          </td>

          <td>{{ item.Type }}</td> <!-- No editable -->

          <td v-if="editId !== item.id">
            {{ item.Type === 'armadura' ? item.AC : item.Damage }}
          </td>
          <td v-else>
            <input
              v-if="editItem.Type === 'armadura'"
              v-model="editItem.AC"
              type="number"
              min="0"
            />
            <input
              v-else
              v-model="editItem.Damage"
              type="text"
            />
          </td>

          <td v-if="editId !== item.id">{{ item.Weight }}</td>
          <td v-else>
            <input v-model.number="editItem.Weight" type="number" min="0" />
          </td>

          <td v-if="editId !== item.id">{{ item.Properties }}</td>
          <td v-else><input v-model="editItem.Properties" /></td>

          <td>
            <button
              v-if="editId !== item.id"
              @click="startEdit(item)"
              class="btn-accion btn-actualizar"
            >Actualizar</button>
            <button
              v-else
              @click="saveEdit(item.id)"
              class="btn-accion btn-guardar"
            >Guardar</button>
            <button
              v-if="editId === item.id"
              @click="cancelEdit"
              class="btn-accion btn-cancelar"
            >Cancelar</button>
            <button
              v-if="editId !== item.id"
              @click="askDelete(item)"
              class="btn-accion btn-eliminar"
            >Eliminar</button>
            <button
              v-if="editId !== item.id"
              @click="showPreview(item)"
              class="btn-accion btn-preview"
            >Vista Previa</button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Modal de Vista Previa -->
    <div v-if="previewItem" class="modal-preview" @click.self="closePreview">
      <div class="modal-content">
        <h3>{{ previewItem.Name }}</h3>
        <img v-if="previewItem.img" :src="previewItem.img" alt="Imagen">
        <ul>
          <li><b>Precio:</b> {{ previewItem.Price }}</li>
          <li><b>Tipo:</b> {{ previewItem.Type }}</li>
          <li><b>AC:</b> {{ previewItem.AC }}</li>
          <li><b>Daño:</b> {{ previewItem.Damage }}</li>
          <li><b>Peso:</b> {{ previewItem.Weight }}</li>
          <li><b>Propiedades:</b> {{ previewItem.Properties }}</li>
        </ul>
        <button @click="closePreview" class="btn-accion btn-cancelar">Cerrar</button>
      </div>
    </div>

    <!-- Modal de Confirmación Eliminar -->
    <div v-if="deleteConfirmItem" class="modal-preview" @click.self="closeDeleteConfirm">
      <div class="modal-content">
        <h3>¿Seguro que quieres eliminar este ítem?</h3>
        <p><b>{{ deleteConfirmItem.Name }}</b></p>
        <button @click="confirmDelete" class="btn-accion btn-guardar">Sí</button>
        <button @click="closeDeleteConfirm" class="btn-accion btn-cancelar">No</button>
      </div>
    </div>
  </div>
</template>

<script>
import itemsAPI from '../../services/itemsAPI';

export default {
  data() {
    return {
      items: [],
      searchQuery: "",
      filterType: "",
      editId: null,
      editItem: {},
      previewItem: null,
      deleteConfirmItem: null, // Para el modal de confirmación
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
      this.$router.push("/add-item");
    },
    async fetchItems() {
      try {
        this.items = await itemsAPI.getItems();
      } catch (error) {
        console.error("Error al obtener los ítems:", error);
      }
    }, 
    startEdit(item) {
      this.editId = item.id;
      this.editItem = { ...item };
    },
    async saveEdit(id) {
      try {
        const itemToUpdate = { ...this.editItem };
        delete itemToUpdate.id;
        itemToUpdate.Price = String(itemToUpdate.Price);
        itemToUpdate.Weight = String(itemToUpdate.Weight);
        await itemsAPI.updateItem(id, itemToUpdate);
        await this.fetchItems();
        this.editId = null;
        this.editItem = {};
      } catch (error) {
        alert("Error al actualizar el ítem");
      }
    },
    cancelEdit() {
      this.editId = null;
      this.editItem = {};
    },
    askDelete(item) {
      this.deleteConfirmItem = item;
    },
    closeDeleteConfirm() {
      this.deleteConfirmItem = null;
    },
    async confirmDelete() {
      try {
        await itemsAPI.deleteItem(this.deleteConfirmItem.id);
        await this.fetchItems();
        this.deleteConfirmItem = null;
      } catch (error) {
        alert("Error al eliminar el ítem");
      }
    },
    showPreview(item) {
      this.previewItem = item;
    },
    closePreview() {
      this.previewItem = null;
    },
  },
  mounted() {
    this.fetchItems();
  },
};
</script>

<style scoped>
  @import "../../assets/css/ItemsStyles/ItemsStyle.css";


</style>