import api from './api';

class Item {
    constructor(id, Name, Price, AC, Damage, Weight, Type, Properties, img) {
        this.id = id;
        this.Name = Name;
        this.Price = Price;
        this.AC = AC;
        this.Damage = Damage;
        this.Weight = Weight;
        this.Type = Type;
        this.Properties = Properties;
        this.img = img;
    }

    toJSON() {
        return {
            id: this.id,
            Name: this.Name,
            Price: this.Price,
            AC: this.AC,
            Damage: this.Damage,
            Weight: this.Weight,
            Type: this.Type,
            Properties: this.Properties,
            img: this.img
        };
    }

    static fromJSON(json) {
        return new Item(
            json.id,
            json.Name,
            json.Price,
            json.AC,
            json.Damage,
            json.Weight,
            json.Type,
            json.Properties,
            json.img
        );
    }
    
}

const getItems = async () => {
    try {
        const response = await api.get('/items');
        return response.data.map(item => Item.fromJSON(item));
    } catch (error) {
        console.error('Error al obtener los items:', error);
        throw error;
    }
};

// Obtener un item por su ID
const getItemById = async (itemId) => {
    try {
        const response = await api.get(`/items/${itemId}`);
        return Item.fromJSON(response.data);
    } catch (error) {
        console.error(`Error al obtener el item con ID ${itemId}:`, error);
        throw error;
    }
};

// Obtener un item por su nombre
const getItemByName = async (itemName) => {
    try {
        const response = await api.get(`/items/${itemName}`);
        return Item.fromJSON(response.data);
    } catch (error) {
        console.error(`Error al obtener el item con nombre ${itemName}:`, error);
        throw error;
    }
};

// Crear un nuevo item
const createItem = async (itemData) => {
    try {
        const response = await api.post('/items', itemData);
        return Item.fromJSON(response.data);
    } catch (error) {
        console.error('Error al crear un nuevo item:', error);
        throw error;
    }
};

// Eliminar un item por su ID
const deleteItem = async (itemId) => {
    try {
        const response = await api.delete(`/items/${itemId}`);
        return response.data;
    } catch (error) {
        console.error(`Error al eliminar el item con ID ${itemId}:`, error);
        throw error;W
    }
};

const updateItem = async (itemId, itemData) => {
    try {
        const response = await api.put(`/items/${itemId}`, itemData);
        return Item.fromJSON(response.data);
    } catch (error) {
        console.error(`Error al actualizar el item con ID ${itemId}:`, error);
        throw error;
    }
};

export default{
    Item,
    getItems,
    getItemById,
    getItemByName,
    createItem,
    deleteItem,
    updateItem
}