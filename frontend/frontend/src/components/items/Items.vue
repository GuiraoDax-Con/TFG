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
          <option value="magia">Magia</option>
          <option value="aventuras">Aventuras</option>
        </select>
      </div>
    </div>

    <!-- Botón para añadir ítems -->
    <div class="add-item-container">
      <button @click="addItem" class="btn-añadir">Añadir Ítem</button>
    </div>

    <!-- Tabla de ítems -->
    <div class="table-responsive">
      <table>
        <thead>
          <tr class="primary-color">
            <th>Seleccionar</th>
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
          <tr v-for="item in paginatedItems" :key="item.id" class="item-row">
            <td>
              <input
                type="checkbox"
                :value="item.id"
                v-model="selectedItems"
              />
            </td>
            <td>
              <img v-if="item.img && editId !== item.id" :src="item.img" alt="Imagen" style="max-width: 50px; max-height: 50px;" />
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
              <div class="acciones-btns">
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
                >Detalles</button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Botón Deseleccionar -->
    <div style="margin-top: 12px; text-align: right;">
      <button
        @click="deseleccionar"
        :disabled="selectedItems.length === 0"
        class="btn-accion btn-cancelar deseleccionar-btn"
      >
        Deseleccionar
      </button>
    </div>

    

    <!-- Modal de Factura -->
    <div class="factura-contenedor">
        <!-- Botón calcular factura flotante -->
        <button
          :disabled="selectedItems.length === 0"
          @click="mostrarFactura = true"
          class="btn-factura-flotante"
        >
          Calcular factura
        </button>

        <div v-if="mostrarFactura" class="factura-contenedor" @click.self="mostrarFactura = false">
          <div class="modal-content">
            <h3>Factura</h3>
            <ul>
              <li v-for="item in selectedInvoiceItems" :key="item.id">
                {{ item.Name }} - {{ item.Price }} monedas
              </li>
            </ul>
            <p><b>Total:</b> {{ facturaTotalMonedas }}</p>
            <button @click="mostrarFactura = false" class="btn-accion btn-cancelar">Cerrar</button>
          </div>
        </div>
    </div>

    <!-- Modal que muestra el total de XP calculado -->
    <!-- <div class="xp-info">
        <button @click="mostrarModuloReparto = true" class="xp-total-button">
            Total: {{ XP_total }} XP
        </button>

        <div v-if="mostrarModuloReparto" class="modulo-reparto">
            <div class="modulo-contenido">
                <div class="jugadores-input">
                    <label for="num-jugadores">Jugadores:</label>
                    <button @click="decrementarJugadores">-</button>
                    <input
                        id="num-jugadores"
                        type="number"
                        v-model.number="numJugadores"
                        min="1"
                    />
                    <button @click="incrementarJugadores">+</button>
                </div>
                <hr />
                <div class="xp-repartido">
                    XP Repartido: {{ XP_repartido }} XP
                </div>
                <button @click="mostrarModuloReparto = false" class="cerrar-modulo">Cerrar</button>
            </div>
        </div>
      </div>
     -->

    <!-- CONTROLES DE PAGINACIÓN -->
    <div v-if="totalPages > 1" class="pagination-controls" style="margin: 16px 0; display: flex; justify-content: center; gap: 4px;">
      <button @click="goToPage(currentPage - 1)" :disabled="currentPage === 1">Anterior</button>
      <button
        v-if="currentPage > 3"
        @click="goToPage(1)"
        :class="{ activo: currentPage === 1 }"
      >1</button>
      <span v-if="currentPage > 4" aria-disabled="true">...</span>
      <button
        v-for="page in pageNumbers"
        :key="page"
        @click="goToPage(page)"
        :class="{ activo: page === currentPage }"
      >{{ page }}</button>
      <span v-if="currentPage < totalPages - 3" aria-disabled="true">...</span>
      <button
        v-if="currentPage < totalPages - 2"
        @click="goToPage(totalPages)"
        :class="{ activo: currentPage === totalPages }"
      >{{ totalPages }}</button>
      <button @click="goToPage(currentPage + 1)" :disabled="currentPage === totalPages">Siguiente</button>
    </div>

    <!-- Modal de Detalles -->
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
      deleteConfirmItem: null,
      // PAGINACIÓN
      currentPage: 1,
      itemsPerPage: 10,
      // Selección para factura
      selectedItems: [],
      mostrarFactura: false,
    };
  },
  computed: {
    filteredItems() {
      return this.items.filter((item) => {
        const matchesName = item.Name.toLowerCase().includes(
          this.searchQuery.toLowerCase()
        );
        let matchesType = true;
        if (this.filterType !== "") {
          const type = item.Type ? item.Type.toLowerCase() : "";
          const filter = this.filterType.toLowerCase();

          if (filter === "arma") {
            // "arma" o "armas" pero NO "armadura"
            matchesType = /\barma(s)?\b/.test(type);
          } else if (filter === "armadura") {
            matchesType = /\barmadura(s)?\b/.test(type);
          } else if (filter === "magia") {
            // magia, mágico, magico, magic
            matchesType = /\bmagia\b|\bmágico\b|\bmagico\b|\bmagic\b/.test(type);
          } else if (filter === "aventuras") {
            // aventuras, adventuring
            matchesType = /\baventura(s)?\b|\badventuring\b/.test(type);
          } else {
            // Por si agregas más tipos en el futuro
            const regex = new RegExp(`\\b${filter}\\b`, "i");
            matchesType = regex.test(type);
          }
        }
        return matchesName && matchesType;
      });
    },
    paginatedItems() {
      const start = (this.currentPage - 1) * this.itemsPerPage;
      const end = start + this.itemsPerPage;
      return this.filteredItems.slice(start, end);
    },
    totalPages() {
      return Math.ceil(this.filteredItems.length / this.itemsPerPage);
    },
    pageNumbers() {
      // Muestra la página currentPage, dos antes y dos después
      const pages = [];
      for (
        let i = Math.max(2, this.currentPage - 2);
        i <= Math.min(this.totalPages - 1, this.currentPage + 2);
        i++
      ) {
        pages.push(i);
      }
      return pages;
    },
    selectedInvoiceItems() {
      return this.items.filter(item => this.selectedItems.includes(item.id));
    },
    invoiceTotal() {
      return this.selectedInvoiceItems.reduce((sum, item) => sum + Number(item.Price), 0);
    },
    facturaTotalMonedas() {
      return this.sumarPreciosPorMoneda(this.selectedInvoiceItems);
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
    goToPage(page) {
      if (page >= 1 && page <= this.totalPages) {
        this.currentPage = page;
      }
    },
    deseleccionar() {
      this.selectedItems = [];
    },
    sumarPreciosPorMoneda(items) {
      // Soporta pl, po, gp, pp, pc
      const monedas = { pl: 0, po: 0, gp: 0, pp: 0, pc: 0 };
      items.forEach(item => {
        if (!item.Price) return;
        // Busca todos los patrones como 3pl, 4po, etc.
        const matches = item.Price.toLowerCase().match(/(\d+)\s*(pl|po|gp|pp|pc)/g);
        if (!matches) return;
        matches.forEach(match => {
          const parts = match.match(/(\d+)\s*(pl|po|gp|pp|pc)/);
          if (!parts) return;
          const value = parseInt(parts[1]);
          const moneda = parts[2];
          if (monedas[moneda] !== undefined) {
            monedas[moneda] += value;
          }
        });
      });
      // Devuelve solo las monedas que tengan valor, en orden típico
      return Object.entries(monedas)
        .filter(([_, v]) => v > 0)
        .map(([k, v]) => `${v}${k}`)
        .join(" y ");
    },
  },
  watch: {
    // Reinicia a la página 1 si cambian los filtros o búsqueda
    searchQuery() {
      this.currentPage = 1;
    },
    filterType() {
      this.currentPage = 1;
    },
  },
  mounted() {
    this.fetchItems();
  },
};
</script>

<style scoped>
  @import "../../assets/css/ItemsStyles/ItemsStyle.css";

.deseleccionar-btn {
  padding: 12px 28px;
  font-size: 1.1em;
}
</style>