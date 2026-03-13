import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:8000/api"
});

export const analyzeEmergency = async (message, age) => {

  const response = await API.post("/emergency/analyze", {
    message,
    age
  });

  return response.data;
};