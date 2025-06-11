// src/services/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'https://tfg-aqbe.onrender.com', // ajusta según tu configuración
  // baseURL: 'http://127.0.0.1:8000',
  headers: {
      'Content-Type': 'application/json'
  }
});

export default api;
