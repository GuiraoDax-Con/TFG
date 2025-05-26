<template>
    <div class="body-page">

        <h1>Calcular XP</h1><br>        

        <div class="filtros-busqueda">
            <div class="barra-busqueda">
                <input
                    type="text"
                    v-model="busqueda"
                    placeholder="Buscar monstruo por nombre..."
                    class="barra-busqueda-input"
                />
            </div>
            <div class="filtro">
                <label for="tamaño">Tamaño:</label>
                <select id="tamaño" v-model="filtroTamaño" >
                    <option value="">Todos</option>
                    <option value="Pequeño">Pequeño</option>
                    <option value="Mediano">Mediano</option>
                    <option value="Grande">Grande</option>
                    <option value="Enorme">Enorme</option>
                    <option value="Colosal">Colosal</option>
                </select>
            </div>
            <div class="filtro">
                <label for="tipo">Tipo:</label>
                <select id="tipo" v-model="filtroTipo" >
                    <option value="">Todos</option>
                    <option value="Humanoide">Humanoide</option>
                    <option value="Gigante">Gigante</option>
                    <option value="Dragón">Dragón</option>
                    <option value="No Muerto">No Muerto</option>
                    <option value="Monstruosidad">Monstruosidad</option>
                    <option value="Constructo">Constructo</option>
                    <option value="Elemental">Elemental</option>
                    <option value="Aberración">Aberración</option>
                </select>
            </div>
            <div class="filtro">
                <label for="orden">Ordenar por nombre:</label>
                <select id="orden" v-model="ordenNombre" @change="aplicarOrden">
                    <option value="asc">Ascendente</option>
                    <option value="desc">Descendente</option>
                </select>
            </div>
        </div>

        <div class="add-container">
            <button @click="monstruosSeleccionados = []" class="btn-limpiar">
                Limpiar Selección
            </button>
            <button @click="addMonster" class="btn-añadir">
                Añadir monstruo
            </button>
        </div>
        

        <div>
            <table>
                <thead>
                    <tr class="primary-color">
                        <th>Select</th>
                        <th>Cantidad</th>
                        <th>Nombre</th>
                        <th>Tamaño</th>
                        <th>Tipo</th>
                        <th>Raza</th>
                        <th>CR</th>
                        <th>XP</th>
                        <th>Acciones</th> <!-- Nueva columna -->
                    </tr>
                </thead>
                
                <tbody>
                    <tr v-for="monstruo in monstruosPaginados" :key="monstruo.id">
                        <td>
                            <input
                                type="checkbox"
                                :checked="monstruosSeleccionados.includes(monstruo)"
                                @change="toggleMonstruo(monstruo)"
                            />
                        </td>
                        <td>
                            <input
                                type="number"
                                v-model.number="monstruo.cantidad"
                                min="1"
                                @change="monstruo.cantidad = Math.max(1, Math.round(monstruo.cantidad)); calcularTotalXP()"
                                class="cantidad-input"
                                :disabled="editId === monstruo.id"
                            />
                        </td>
                        <!-- Nombre -->
                        <td v-if="editId !== monstruo.id">{{ monstruo.name }}</td>
                        <td v-else><input v-model="editMonstruo.name" /></td>
                        <!-- Tamaño -->
                        <td v-if="editId !== monstruo.id">{{ monstruo.size }}</td>
                        <td v-else><input v-model="editMonstruo.size" /></td>
                        <!-- Tipo -->
                        <td v-if="editId !== monstruo.id">{{ monstruo.type }}</td>
                        <td v-else><input v-model="editMonstruo.type" /></td>
                        <!-- Raza -->
                        <td v-if="editId !== monstruo.id">{{ monstruo.tag }}</td>
                        <td v-else><input v-model="editMonstruo.tag" /></td>
                        <!-- CR -->
                        <td v-if="editId !== monstruo.id">{{ monstruo.cr }}</td>
                        <td v-else><input v-model="editMonstruo.cr" /></td>
                        <!-- XP -->
                        <td>{{ calcularXP(monstruo.cr) * monstruo.cantidad }}</td>
                        <!-- Acciones -->
                        <td>
                            <div class="acciones-btns">
                                <button
                                    v-if="editId !== monstruo.id"
                                    @click="startEdit(monstruo)"
                                    class="btn-accion btn-actualizar"
                                >Actualizar</button>
                                <button
                                    v-else
                                    @click="saveEdit(monstruo.id)"
                                    class="btn-accion btn-guardar"
                                >Guardar</button>
                                <button
                                    v-if="editId === monstruo.id"
                                    @click="cancelEdit"
                                    class="btn-accion btn-cancelar"
                                >Cancelar</button>
                                <button
                                    v-if="editId !== monstruo.id"
                                    @click="() => { console.log('Click eliminar'); askDelete(monstruo); }"
                                    class="btn-accion btn-eliminar"
                                >Eliminar</button>
                                <button
                                    v-if="editId !== monstruo.id"
                                    @click="() => { console.log('Click detalles'); showPreview(monstruo); }"
                                    class="btn-accion btn-preview"
                                >Detalles</button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Modal que muestra el total de XP calculado -->
        <div class="contenedor-calculadora">
            <button @click="mostrarModuloReparto = true" class="btn-calculadora-flotante">
                Total: {{ XP_total }} XP
            </button>

            <div v-if="mostrarModuloReparto" class="modulo-calculo">
                <div class="modulo-contenido">
                    <div class="jugadores-input">
                        <label for="num-jugadores">Jugadores:</label>
                        <button @click="decrementarJugadores">-</button>
                        <input
                            id="num-jugadores"
                            type="number"
                            @change="numJugadores = Math.max(1, Math.round(numJugadores))"
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

        <!-- Modal de Detalles -->
        <div v-if="previewMonstruo" class="modal-preview" @click.self="closePreview">
            <div class="modal-content">
                <h3>{{ previewMonstruo.name }}</h3>
                <iframe v-if="previewMonstruo.img" :src="previewMonstruo.img" alt="Imagen" class="img-detalles"  scrolling="no" allowfullscreen :title="previewMonstruo.name" ></iframe>
                <ul>
                    <!-- <li><b>URL:</b> {{ previewMonstruo.img }}</li> -->
                    <li><b>Tamaño:</b> {{ previewMonstruo.size }}</li>
                    <li><b>Tipo:</b> {{ previewMonstruo.type }}</li>
                    <li><b>Raza:</b> {{ previewMonstruo.tag }}</li>
                    <li><b>CR:</b> {{ previewMonstruo.cr }}</li>
                    <li><b>XP:</b> {{ calcularXP(previewMonstruo.cr) }}</li>
                    <li><b>Libro:</b> {{ previewMonstruo.sourceBook }}</li>
                    <li v-if="previewMonstruo.descripcion"><b>Descripción:</b> {{ previewMonstruo.descripcion }}</li>
                </ul>
                <button @click="closePreview" class="btn-accion btn-cancelar">Cerrar</button>
            </div>
        </div>

        <!-- Modal de Confirmación Eliminar -->
        <div v-if="deleteConfirmMonstruo" class="modal-preview" @click.self="closeDeleteConfirm">
            <div class="modal-content">
                <h3>¿Seguro que quieres eliminar este monstruo?</h3>
                <p><b>{{ deleteConfirmMonstruo.name }}</b></p>
                <button @click="confirmDelete" class="btn-accion btn-guardar">Sí</button>
                <button @click="closeDeleteConfirm" class="btn-accion btn-cancelar">No</button>
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
</template>

<script>
    import {ref, computed } from 'vue';
    import { useRouter } from 'vue-router';
    import listaMosntruos from "@/services/monstersAPI.js"; // Importa la lista de monstruos desde el API

    export default {
        data() {
            return {
                monstruos: [],
                xp_diccionary: {
                    "1/8": 25,
                    "1/4": 50,
                    "1/2": 100,
                    1: 200,
                    2: 450,
                    3: 700,
                    4: 1100,
                    5: 1800,
                    6: 2300,
                    7: 2900,
                    8: 3900,
                    9: 5000,
                    10: 5900,
                    11: 7200,
                    12: 8400,
                    13: 10000,
                    14: 11500,
                    15: 13000,
                    16: 15000,
                    17: 18000,
                    18: 20000,
                    19: 22000,
                    20: 25000,
                    21: 33000,
                    22: 41000,
                    23: 50000,
                    24: 62000,
                    25: 75000,
                    26: 90000,
                    27: 105000,
                    28: 120000,
                    29: 135000,
                    30: 155000
                },
                multiplicadorXP: {
                    1: 1,
                    2: 1.5,
                    3: 2,
                    7: 2.5,
                    11: 3,
                    15: 4
                },
                monstruosSeleccionados: [],
                numJugadores: 4,
                mostrarModuloReparto: false,
                busqueda: '', // Agregamos la propiedad para la búsqueda
                filtroTamaño: '',
                filtroTipo: '',
                ordenNombre: "asc", // Nuevo: Controla el orden de los nombres
                editId: null,
                editMonstruo: {},
                previewMonstruo: null,
                deleteConfirmMonstruo: null,
                paginaActual: 1,
                monstruosPorPagina: 10,
            };
        },
        computed: {
            monstruosFiltrados() {
                // Filtra los monstruos por nombre, tamaño y tipo
                let filtrados = this.monstruos;

                const busquedaMinuscula = this.busqueda.toLowerCase();
                filtrados = filtrados.filter(monstruo =>
                    monstruo.name.toLowerCase().includes(busquedaMinuscula)
                );

                if (this.filtroTamaño) {
                    filtrados = filtrados.filter(monstruo => monstruo.size === this.filtroTamaño);
                }

                if (this.filtroTipo) {
                    filtrados = filtrados.filter(monstruo => monstruo.type === this.filtroTipo);
                }

                // Ordenar por nombre
                if (this.ordenNombre === "asc") {
                    filtrados.sort((a, b) => a.name.localeCompare(b.name));
                } else if (this.ordenNombre === "desc") {
                    filtrados.sort((a, b) => b.name.localeCompare(a.name));
                }

                return filtrados;
            },
            XP_total() {
                const xpSinMultiplicador = this.monstruosSeleccionados.reduce((total, monstruo) => {
                    return total + this.calcularXP(monstruo.cr) * monstruo.cantidad;
                }, 0);

                const cantidadTotal = this.monstruosSeleccionados.reduce((suma, m) => suma + m.cantidad, 0);
                const multiplicador = this.calcularMultiplicadorXP(cantidadTotal);

                return Math.ceil(xpSinMultiplicador * multiplicador);
            },
            XP_repartido() {
                return Math.ceil(this.XP_total / this.numJugadores);
            },
            totalPages() {
                return Math.ceil(this.monstruosFiltrados.length / this.monstruosPorPagina);
            },
            monstruosPaginados() {
                const inicio = (this.paginaActual - 1) * this.monstruosPorPagina;
                const fin = inicio + this.monstruosPorPagina;
                return this.monstruosFiltrados.slice(inicio, fin);
            },
            watch: {
                busqueda() { this.paginaActual = 1; },
                filtroTamaño() { this.paginaActual = 1; },
                filtroTipo() { this.paginaActual = 1; },
                ordenNombre() { this.paginaActual = 1; },
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
            addMonster() {
                console.log("Ir a la zona de añadir monstruos");
                this.$router.push("/add-monster");
            },
            async fetchMonstruos() {
                try {
                    const monstruos = await listaMosntruos.getMonsters();
                    this.monstruos = monstruos.map((monstruo, index) => ({
                        ...monstruo,
                        id: monstruo.id || index, // Asegura que siempre haya un id
                        cantidad: 1, // Inicializa la cantidad en 1
                    }));
                } catch (error) {
                    console.error("Error al obtener los monstruos:", error);
                }
            },
            calcularXP(cr) {
                return this.xp_diccionary[cr] || 0;
            },
            toggleMonstruo(monstruo) {
                const index = this.monstruosSeleccionados.findIndex(m => m.id === monstruo.id);
                if (index !== -1) {
                    this.monstruosSeleccionados.splice(index, 1);
                } else {
                    this.monstruosSeleccionados.push(monstruo);
                }
                this.calcularTotalXP(); // Recalcular el total al seleccionar/deseleccionar
            },
            incrementarJugadores() {
                this.numJugadores++;
            },
            decrementarJugadores() {
                if (this.numJugadores > 1) {
                    this.numJugadores--;
                }
            },
            calcularMultiplicadorXP(cantidadTotal) {
                if (cantidadTotal === 1) return 1;
                if (cantidadTotal === 2) return 1.5;
                if (cantidadTotal >= 3 && cantidadTotal <= 6) return 2;
                if (cantidadTotal >= 7 && cantidadTotal <= 10) return 2.5;
                if (cantidadTotal >= 11 && cantidadTotal <= 14) return 3;
                return 4; // 15 o más jugadores
            },
            calcularTotalXP() {
                // Método para recalcular el XP total.  Se llama cuando cambia la cantidad de monstruos.
                this.XP_total;
            },
            startEdit(monstruo) {
                this.editId = monstruo.id;
                this.editMonstruo = { ...monstruo };
            },
            async saveEdit(id) {
                try {
                    const monstruoToUpdate = { ...this.editMonstruo };
                    delete monstruoToUpdate.id;
                    await listaMosntruos.updateMonster(id, monstruoToUpdate);
                    await this.fetchMonstruos();
                    this.editId = null;
                    this.editMonstruo = {};
                } catch (error) {
                    alert("Error al actualizar el monstruo");
                }
            },
            cancelEdit() {
                this.editId = null;
                this.editMonstruo = {};
            },
            askDelete(monstruo) {
                console.log("Eliminar monstruo:", monstruo); // DEBUG
                this.deleteConfirmMonstruo = monstruo;
                console.log("Monstruo a eliminar:", this.deleteConfirmMonstruo); // DEBUG
            },
            closeDeleteConfirm() {
                console.log("Cerrar confirmación de eliminación"); // DEBUG
                this.deleteConfirmMonstruo = null;
            },
            async confirmDelete() {
                console.log("Confirmar eliminación de monstruo:", this.deleteConfirmMonstruo); // DEBUG
                try {
                    await listaMosntruos.deleteMonster(this.deleteConfirmMonstruo.id);
                    await this.fetchMonstruos();
                    this.deleteConfirmMonstruo = null;
                } catch (error) {
                    alert("Error al eliminar el monstruo");
                }
            },
            showPreview(monstruo) {
                console.log("Mostrar detalles del monstruo:", monstruo); // DEBUG
                this.previewMonstruo = monstruo;
            },
            closePreview() {
                this.previewMonstruo = null;
            },
            prevPage() {
                if (this.paginaActual > 1) this.paginaActual--;
            },
            nextPage() {
                if (this.paginaActual < this.totalPages) this.paginaActual++;
            },
        },
        mounted() {
            this.fetchMonstruos();
        }
    };
</script>

<style>
    @import "@/assets/css/MonstersStyles/CalcularXPStyle.css";
</style>
