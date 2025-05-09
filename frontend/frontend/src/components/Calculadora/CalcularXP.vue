<template>
    <div class="calcular-xp">

        <div class="logo-container-calculadoraxp">
            <img :src="calXP_logo" alt="Escudo del Bestiario" 
            class="main-logo-calculadoraxp" />
        </div>

        <h1>Calcular XP</h1>

        <div class="filtros-busqueda">
            <div class="busqueda-monstruos">
                <input
                    type="text"
                    v-model="busqueda"
                    placeholder="Buscar monstruo por nombre..."
                    class="busqueda-input"
                />
            </div>
            <div class="filtro-tamaño">
                <label for="tamaño">Tamaño:</label>
                <select id="tamaño" v-model="filtroTamaño" @change="aplicarFiltros">
                    <option value="">Todos</option>
                    <option value="Pequeño">Pequeño</option>
                    <option value="Mediano">Mediano</option>
                    <option value="Grande">Grande</option>
                    <option value="Enorme">Enorme</option>
                    <option value="Gargantuesco">Gargantuesco</option>
                </select>
            </div>
            <div class="filtro-tipo">
                <label for="tipo">Tipo:</label>
                <select id="tipo" v-model="filtroTipo" @change="aplicarFiltros">
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
        </div>

        <div class="add-monster-container">
            <button @click="monstruosSeleccionados = []" class="btn-limpiar">
                Limpiar Selección
            </button>
            <button @click="abrirModal = true" class="btn-añadir-monstruo">
                Añadir monstruo
            </button>
        </div>

        <!-- Modal -->
        <div v-if="abrirModal" class="modal-overlay">
            <div class="modal-content">
                <h2>Añadir nuevo monstruo</h2>
                <form @submit.prevent="guardarMonstruo">
                    <input v-model="nuevoMonstruo.name" type="text" placeholder="Nombre *" required />
                    <input v-model="nuevoMonstruo.size" type="text" placeholder="Tamaño *" required />
                    <input v-model="nuevoMonstruo.type" type="text" placeholder="Tipo *" required />
                    <input v-model="nuevoMonstruo.tag" type="text" placeholder="Raza" />
                    <input v-model="nuevoMonstruo.alignment" type="text" placeholder="Alineamiento" />
                    <input v-model="nuevoMonstruo.cr" type="text" placeholder="CR *" required />
                    <input v-model="nuevoMonstruo.sourceBook" type="text" placeholder="Libro Origen" />
                    <input @change="handleImageUpload" type="file" accept="image/png, image/jpeg" />
                    <div class="modal-buttons">
                        <button type="submit">Guardar</button>
                        <button @click.prevent="abrirModal = false">Cancelar</button>
                    </div>
                </form>
            </div>
        </div>
        <!-- Fin del Modal -->

        <div class="tabla-monstruos">
            <table>
                <thead>
                    <tr>
                        <th>Seleccionar</th>
                        <th>Cantidad</th>
                        <th>Nombre</th>
                        <th>Tamaño</th>
                        <th>Tipo</th>
                        <th>Raza</th>
                        <th>CR</th>
                        <th>XP</th>
                    </tr>
                </thead>
                
                <tbody>
                    <tr v-for="monstruo in monstruosFiltrados" :key="monstruo.nombre">
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
                                @change="calcularTotalXP"
                                class="cantidad-input"
                            />
                        </td>
                        <td>{{ monstruo.nombre }}</td>
                        <td>{{ monstruo.tamaño }}</td>
                        <td>{{ monstruo.tipo }}</td>
                        <td>{{ monstruo.raza }}</td>
                        <td>{{ monstruo.cr }}</td>
                        <td>{{ calcularXP(monstruo.cr) * monstruo.cantidad }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="xp-info">
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
    </div>
</template>

<script>
    import calXP_logo from "@/assets/images/calculadora-xp_imagenes/imagen_calculadora-xp.png"; // Importa la imagen
    //import { useAddMonster } from "@/composables/useAddMonster.js";

    export default {
        data() {
            return {
                monstruos: [
                    { nombre: "Goblin", cr: "1/4", cantidad: 1, tamaño: "Pequeño", tipo: "Humanoide", raza: "Goblinoide" },
                    { nombre: "Orco", cr: "1/2", cantidad: 1, tamaño: "Mediano", tipo: "Humanoide", raza: "Orcoide" },
                    { nombre: "Ogro", cr: 2, cantidad: 1, tamaño: "Grande", tipo: "Gigante", raza: "" },
                    { nombre: "Dragón Rojo Adulto", cr: 17, cantidad: 1, tamaño: "Enorme", tipo: "Dragón", raza: "Dracónico" },
                    { nombre: "Esqueleto", cr: "1/4", cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Zombi", cr: "1/4", cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Ghoul", cr: 1, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Espectro", cr: 13, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "Incorpóreo" },
                    { nombre: "Vampiro", cr: 13, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "Cambiaformas" },
                    { nombre: "Manticora", cr: 3, cantidad: 1, tamaño: "Grande", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Basilisco", cr: 3, cantidad: 1, tamaño: "Mediano", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Golem de Piedra", cr: 7, cantidad: 1, tamaño: "Grande", tipo: "Constructo", raza: "" },
                    { nombre: "Golem de Acero", cr: 10, cantidad: 1, tamaño: "Grande", tipo: "Constructo", raza: "" },
                    { nombre: "Golem de Tierra", cr: 10, cantidad: 1, tamaño: "Grande", tipo: "Constructo", raza: "" },
                    { nombre: "Griffon", cr: 3, cantidad: 1, tamaño: "Grande", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Quimera", cr: 3, cantidad: 1, tamaño: "Grande", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Hidra", cr: 8, cantidad: 1, tamaño: "Enorme", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Kraken", cr: 20, cantidad: 1, tamaño: "Gargantuesco", tipo: "Monstruosidad", raza: "Acuático" },
                    { nombre: "Troll", cr: 5, cantidad: 1, tamaño: "Grande", tipo: "Gigante", raza: "" },
                    { nombre: "Gárgola", cr: 2, cantidad: 1, tamaño: "Mediano", tipo: "Elemental", raza: "" },
                    { nombre: "Minotauro", cr: 3, cantidad: 1, tamaño: "Grande", tipo: "Monstruosidad", raza: "" },
                    { nombre: "Banshee", cr: 4, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Múmia", cr: 5, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Lich", cr: 21, cantidad: 1, tamaño: "Mediano", tipo: "No Muerto", raza: "" },
                    { nombre: "Beholder", cr: 13, cantidad: 1, tamaño: "Grande", tipo: "Aberración", raza: "" },
                ],
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
                monstruosSeleccionados: [],
                numJugadores: 4,
                mostrarModuloReparto: false,
                calXP_logo: calXP_logo, // Asigna la ruta importada a la propiedad data
                busqueda: '', // Agregamos la propiedad para la búsqueda
                filtroTamaño: '',
                filtroTipo: '',
            };
        },
        computed: {
            monstruosFiltrados() {
                // Filtra los monstruos por nombre, tamaño y tipo
                let filtrados = this.monstruos;

                const busquedaMinuscula = this.busqueda.toLowerCase();
                filtrados = filtrados.filter(monstruo =>
                    monstruo.nombre.toLowerCase().includes(busquedaMinuscula)
                );

                if (this.filtroTamaño) {
                    filtrados = filtrados.filter(monstruo => monstruo.tamaño === this.filtroTamaño);
                }

                if (this.filtroTipo) {
                    filtrados = filtrados.filter(monstruo => monstruo.tipo === this.filtroTipo);
                }

                return filtrados;
            },
            XP_total() {
                return this.monstruosSeleccionados.reduce((total, monstruo) => {
                    const xp = this.calcularXP(monstruo.cr) * monstruo.cantidad;
                    return total + xp;
                }, 0);
            },
            XP_repartido() {
                return Math.ceil(this.XP_total / this.numJugadores);
            },
        },
        methods: {
            calcularXP(cr) {
                return this.xp_diccionary[cr] || 0;
            },
            toggleMonstruo(monstruo) {
                if (this.monstruosSeleccionados.includes(monstruo)) {
                    this.monstruosSeleccionados.splice(
                        this.monstruosSeleccionados.indexOf(monstruo),
                        1
                    );
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
            calcularTotalXP() {
                // Método para recalcular el XP total.  Se llama cuando cambia la cantidad de monstruos.
                this.XP_total;
            },
            aplicarFiltros() {
                // Este método se llama cuando cambian los filtros de tamaño o tipo.
                // No es necesario hacer nada aquí, ya que los filtros se aplican directamente
                // en la propiedad computada monstruosFiltrados.
            }
        },
    };

    /* const {
        abrirModal,
        nuevoMonstruo,
        handleImageUpload,
        guardarMonstruo
    } = useAddMonster(); */
</script>

<style scoped>
    @import "@/assets/css/CalculadoraXPcss/CalcularXPStyle.css";
    @import "@/assets/css/CalculadoraXPcss/FiltrosClacXP.css";
</style>
