/* // src/composables/useAddMonster.js
import { ref } from "vue";
import monstersAPI from "../services/monstersAPI.js";

export const useAddMonster = () => {
    const abrirModal = ref(false);
    const nuevoMonstruo = ref({
        name: "",
        size: "",
        type: "",
        tag: "",
        alignment: "",
        cr: "",
        sourceBook: "",
        img: ""
    });

    const handleImageUpload = (event) => {
        const file = event.target.files[0];
        if (file && (file.type === "image/png" || file.type === "image/jpeg")) {
            const reader = new FileReader();
            reader.onload = () => {
                nuevoMonstruo.value.img = reader.result;
            };
            reader.readAsDataURL(file);
        }
    };

    const guardarMonstruo = async () => {
        if (!nuevoMonstruo.value.name || !nuevoMonstruo.value.size || !nuevoMonstruo.value.type || !nuevoMonstruo.value.cr) {
            alert("Por favor completa todos los campos obligatorios.");
            return;
        }

        try {
            await monstersAPI.createMonster({
                name: nuevoMonstruo.value.name,
                size: nuevoMonstruo.value.size,
                type: nuevoMonstruo.value.type,
                tag: nuevoMonstruo.value.tag,
                alignment: nuevoMonstruo.value.alignment,
                cr: nuevoMonstruo.value.cr,
                sourceBook: nuevoMonstruo.value.sourceBook,
                img: nuevoMonstruo.value.img
            });
            alert("Monstruo creado correctamente.");
            abrirModal.value = false;
        } catch (error) {
            console.error("Error al crear monstruo:", error);
            alert("Error al crear monstruo.");
        }
    };

    return {
        abrirModal,
        nuevoMonstruo,
        handleImageUpload,
        guardarMonstruo
    };
};
 */