import React, { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    nombre: "",
    especialidad: "",
    email: "",
    telefono: "",
    horarios_consulta: ""
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch("http://localhost:5000/api/doctores", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Doctor añadido:", data);
        // Aquí podrías redirigir al usuario a otra página o realizar alguna acción adicional
      })
      .catch((error) => {
        console.error("Error al añadir doctor:", error);
      });
  };

  return (
    <div className="App">
      <h1>Añadir Doctor</h1>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input type="text" name="nombre" value={formData.nombre} onChange={handleChange} />
        <label>Especialidad:</label>
        <input type="text" name="especialidad" value={formData.especialidad} onChange={handleChange} />
        <label>Email:</label>
        <input type="email" name="email" value={formData.email} onChange={handleChange} />
        <label>Teléfono:</label>
        <input type="text" name="telefono" value={formData.telefono} onChange={handleChange} />
        <label>Horarios de Consulta:</label>
        <input type="text" name="horarios_consulta" value={formData.horarios_consulta} onChange={handleChange} />
        <button type="submit">Añadir Doctor</button>
      </form>
    </div>
  );
}

export default App;
