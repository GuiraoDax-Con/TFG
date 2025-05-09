import api from './api';

// Constructor de Monster
export class Monster {
    constructor(id, name, size, type, tag, alignment, cr, sourceBook, img) {
        this.id = id; // ID del monstruo
        this.name = name; // Nombre del monstruo
        this.size = size; // Tamaño del monstruo
        this.type = type; // Tipo del monstruo
        this.tag = tag; // Etiqueta del monstruo
        this.alignment = alignment; // Alineación del monstruo
        this.cr = cr; // Challenge Rating (CR) del monstruo
        this.sourceBook = sourceBook; // Libro de origen del monstruo
        this.img = img; // URL o ruta de la imagen del monstruo
    }

    // Método para convertir la instancia a JSON
    toJSON() {
        return {
            id: this.id,
            name: this.name,
            size: this.size,
            type: this.type,
            tag: this.tag,
            alignment: this.alignment,
            cr: this.cr,
            sourceBook: this.sourceBook,
            img: this.img,
        };
    }

    // Método estático para crear un Monster desde un JSON
    static fromJSON(json) {
        return new Monster(
            json.id,
            json.name,
            json.size,
            json.type,
            json.tag,
            json.alignment,
            json.cr,
            json.sourceBook,
            json.img
        );
    }
}


// Obtener todos los monstruos
export const getMonsters = async () => {
    try {
        const response = await api.get('/monsters');
        return response.data;
    } catch (error) {
        console.error('Error al obtener los monstruos:', error);
        throw error;
    }
};

// Obtener un monstruo por su ID
export const getMonsterById = async (monsterId) => {
    try {
        const response = await api.get(`/monsters/${monsterId}`);
        return response.data;
    } catch (error) {
        console.error(`Error al obtener el monstruo con ID ${monsterId}:`, error);
        throw error;
    }
};

// Obtener un monstruo por su nombre
export const getMonsterByName = async (monsterName) => {
    try {
        const response = await api.get(`/monsters/${monsterName}`);
        return response.data;
    } catch (error) {
        console.error(`Error al obtener el monstruo con nombre ${monsterName}:`, error);
        throw error;
    }
};

// Crear un nuevo monstruo
export const createMonster = async (monsterData) => {
    try {
        const response = await api.post('/monsters', monsterData);
        return response.data;
    } catch (error) {
        console.error('Error al crear un nuevo monstruo:', error);
        throw error;
    }
};

// Eliminar un monstruo por su ID
export const deleteMonster = async (monsterId) => {
    try {
        const response = await api.delete(`/monsters/${monsterId}`);
        return response.data;
    } catch (error) {
        console.error(`Error al eliminar el monstruo con ID ${monsterId}:`, error);
        throw error;
    }
};

