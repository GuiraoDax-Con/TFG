// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://tfg-aqbe.onrender.com', // ajusta según tu configuración
  headers: {
      'Content-Type': 'application/json'
  }
});

export default api;
