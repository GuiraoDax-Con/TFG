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
    <div class="add-container">
      <!-- Botón Deseleccionar -->
      <button class="btn-limpiar" @click="deseleccionar" :disabled="selectedItems.length === 0">
        Deseleccionar
      </button>
      
      <button @click="addItem" class="btn-añadir">Añadir Ítem</button>
    </div>

    <!-- Tabla de ítems -->
    <div class="table-responsive">
      <table>
        <thead>
          <tr class="primary-color">
            <th>Selec</th>
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
          <tr v-for="item in itemsPaginados" :key="item.id" class="item-row">
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

    

    <!-- Modal de Factura -->
    <div class="contenedor-calculadora">
        <!-- Botón calcular factura flotante -->
        <button
          :disabled="selectedItems.length === 0"
          @click="mostrarFactura = true"
          class="btn-calculadora-flotante"
        >
          Calcular factura
        </button>

        <div v-if="mostrarFactura" class="contenedor-calculadora" @click.self="mostrarFactura = false">
          <div class="modulo-calculo">
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

    

    <!-- Controles de paginación -->
    <div class="pagination-controls">
        <button @click="prevPage" :disabled="paginaActual === 1">Anterior</button>
        
        <!-- <span>Página {{ paginaActual }} de {{ totalPages }}</span> -->

        <button
            v-for="pagina in paginasVisibles"
            :key="pagina"
            @click="pagina !== '...' && (paginaActual = pagina)"
            :class="[{ activo: pagina === paginaActual }, { 'button-ellipsis': pagina === '...' }]"
            v-if="pagina !== 1 && pagina !== totalPages"
            :disabled="pagina === paginaActual"
        >
            {{ pagina }}
        </button>

        <button @click="nextPage" :disabled="paginaActual === totalPages">Siguiente</button>
    </div>

    <!-- Modal de Detalles -->
    <div v-if="previewItem" class="modal-preview" @click.self="closePreview">
      <div class="modal-content">
        <h3>{{ previewItem.Name }}</h3>
        <img
          v-if="previewItem.img"
          :src="previewItem.img"
          alt="Imagen"
          class="img-detalles"
          scrolling="no"
          allowfullscreen
          :title="previewItem.Name"
        />
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
      paginaActual: 1,
      itemsPorPagina: 10,
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
    itemsPaginados() {
        const inicio = (this.paginaActual - 1) * this.itemsPorPagina;
        const fin = inicio + this.itemsPorPagina;
        return this.filteredItems.slice(inicio, fin);
    },
    totalPages() {
        return Math.ceil(this.filteredItems.length / this.itemsPorPagina);
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
    paginasVisibles() {
        const total = this.totalPages;
        const actual = this.paginaActual;
        const rango = 2; // páginas a la izquierda y derecha

        let inicio = Math.max(1, actual - rango);
        let fin = Math.min(total, actual + rango);

        const paginas = [];

        if (inicio > 1) {
            paginas.push(1);
            if (inicio > 2) paginas.push('...');
        }

        for (let i = inicio; i <= fin; i++) {
            paginas.push(i);
        }

        if (fin < total) {
            if (fin < total - 1) paginas.push('...');
            paginas.push(total);
        }

        return paginas;
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
    prevPage() {
        if (this.paginaActual > 1) this.paginaActual--;
    },
    nextPage() {
        if (this.paginaActual < this.totalPages) this.paginaActual++;
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
</style>