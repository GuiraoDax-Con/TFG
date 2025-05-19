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
                <select id="tamaño" v-model="filtroTamaño" @change="aplicarFiltros">
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
            <div class="filtro">
                <label for="orden">Ordenar por nombre:</label>
                <select id="orden" v-model="ordenNombre" @change="aplicarOrden">
                    <option value="asc">Ascendente</option>
                    <option value="desc">Descendente</option>
                </select>
            </div>
        </div>

        <div class="add-monster-container">
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
                    <tr v-for="monstruo in monstruosFiltrados" :key="monstruo.id">
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
                        <td>{{ monstruo.name }}</td>
                        <td>{{ monstruo.size }}</td>
                        <td>{{ monstruo.type }}</td>
                        <td>{{ monstruo.tag }}</td>
                        <td>{{ monstruo.cr }}</td>
                        <td>{{ calcularXP(monstruo.cr) * monstruo.cantidad }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Modal que muestra el total de XP calculado -->
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
        },
        methods: {
            addMonster() {
                console.log("Ir a la zona de añadir monstruos");
                this.$router.push("/add-monster");
            },
            async fetchMonstruos() {
                try {
                    const monstruos = await listaMosntruos.getMonsters();
                    this.monstruos = monstruos.map((monstruo) => ({
                        ...monstruo,
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
                /*
                if (this.monstruosSeleccionados.includes(monstruo)) {
                    this.monstruosSeleccionados.splice(
                        this.monstruosSeleccionados.indexOf(monstruo),
                        1
                    );
                */
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
                return 4; // 15 o más
            },
            calcularTotalXP() {
                // Método para recalcular el XP total.  Se llama cuando cambia la cantidad de monstruos.
                this.XP_total;
            },
            aplicarFiltros() {
                /* 
                 * Este método se llama cuando cambian los filtros de tamaño o tipo.
                 * No es necesario poner nada aquí, ya que los filtros se aplican directamente
                 * en la propiedad computada monstruosFiltrados.
                 */
            },
            aplicarOrden() {
                // Este método se llama cuando cambia el orden de los nombres.
                // No es necesario poner nada aquí, ya que el orden se aplica directamente
                // en la propiedad computada monstruosFiltrados.
            }
        },
        mounted() {
            this.fetchMonstruos();
        }
    };
</script>

<style scoped>
    @import "@/assets/css/MonstersStyles/CalcularXPStyle.css";
</style>
