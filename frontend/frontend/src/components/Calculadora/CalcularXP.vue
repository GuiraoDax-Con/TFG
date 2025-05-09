<template>
    <div class="calcular-xp">

        <div class="logo-container-calculadoraxp">
            <img :src="calXP_logo" alt="Escudo del Bestiario" 
            class="main-logo-calculadoraxp" />
        </div>

        <h1>Calcular XP</h1>

        <div class="tabla-monstruos">
            <table>
                <thead>
                    <tr>
                        <th>Seleccionar</th>
                        <th>Cantidad</th>
                        <th>Nombre</th>
                        <th>CR</th>
                        <th>XP</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="monstruo in monstruos" :key="monstruo.nombre">
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

    export default {
        data() {
            return {
                monstruos: [
                    { nombre: "Goblin", cr: "1/4", cantidad: 1 },
                    { nombre: "Orco", cr: "1/2", cantidad: 1 },
                    { nombre: "Ogro", cr: 2, cantidad: 1 },
                    { nombre: "Dragón Rojo Adulto", cr: 17, cantidad: 1 },
                    { nombre: "Esqueleto", cr: "1/4", cantidad: 1 },
                    { nombre: "Zombi", cr: "1/4", cantidad: 1 },
                    { nombre: "Ghoul", cr: 1, cantidad: 1 },
                    { nombre: "Espectro", cr: 13, cantidad: 1 },
                    { nombre: "Vampiro", cr: 13, cantidad: 1 },
                    { nombre: "Manticora", cr: 3, cantidad: 1 },
                    { nombre: "Basilisco", cr: 3, cantidad: 1 },
                    { nombre: "Golem de Piedra", cr: 7, cantidad: 1 },
                    { nombre: "Golem de Acero", cr: 10, cantidad: 1 },
                    { nombre: "Golem de Tierra", cr: 10, cantidad: 1 },
                    { nombre: "Griffon", cr: 3, cantidad: 1 },
                    { nombre: "Quimera", cr: 3, cantidad: 1 },
                    { nombre: "Hidra", cr: 8, cantidad: 1 },
                    { nombre: "Kraken", cr: 20, cantidad: 1 },
                    { nombre: "Troll", cr: 5, cantidad: 1 },
                    { nombre: "Gárgola", cr: 2, cantidad: 1 },
                    { nombre: "Minotauro", cr: 3, cantidad: 1 },
                    { nombre: "Banshee", cr: 4, cantidad: 1 },
                    { nombre: "Múmia", cr: 5, cantidad: 1 },
                    { nombre: "Lich", cr: 21, cantidad: 1 },
                    { nombre: "Beholder", cr: 13, cantidad: 1 },
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
            };
        },
        computed: {
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
            }
        },
    };
</script>

<style scoped>
    @import "@/assets/css/CalcularXPStyle.css";
</style>
