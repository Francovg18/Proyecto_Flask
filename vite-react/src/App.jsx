import React, { useState, useEffect } from 'react';
import './App.css'; // Importa tu archivo de estilos CSS

function App() {
  const [doctores, setDoctores] = useState([]);
  const [editDoctor, setEditDoctor] = useState(null);
  const [nuevoDoctor, setNuevoDoctor] = useState({
    nombre: '',
    especialidad: '',
    email: '',
    telefono: '',
    horarios_consulta: ''
  });

  useEffect(() => {
    fetch('http://localhost:5000/api/doctores')
      .then(response => response.json())
      .then(data => setDoctores(data))
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const handleChange = e => {
    const { name, value } = e.target;
    setNuevoDoctor(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = e => {
    e.preventDefault();
    const url = editDoctor ? `http://localhost:5000/api/doctores/${editDoctor.ID_D}` : 'http://localhost:5000/api/doctores';
    const method = editDoctor ? 'PUT' : 'POST';
    fetch(url, {
      method: method,
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(nuevoDoctor)
    })
    .then(response => response.json())
    .then(data => {
      if (editDoctor) {
        setDoctores(doctores.map(doctor => doctor.ID_D === editDoctor.ID_D ? data : doctor));
        setEditDoctor(null);
      } else {
        setDoctores(prevState => [...prevState, data]);
      }
      setNuevoDoctor({
        nombre: '',
        especialidad: '',
        email: '',
        telefono: '',
        horarios_consulta: ''
      });
    })
    .catch(error => console.error('Error creating/updating doctor:', error));
  };

  const handleDelete = id => {
    fetch(`http://localhost:5000/api/doctores/${id}`, {
      method: 'DELETE'
    })
    .then(() => {
      setDoctores(prevState => prevState.filter(doctor => doctor.ID_D !== id));
    })
    .catch(error => console.error('Error deleting doctor:', error));
  };

  const handleEdit = doctor => {
    setNuevoDoctor({
      nombre: doctor.Nombre,
      especialidad: doctor.Especialidad,
      email: doctor.Email,
      telefono: doctor.Teléfono,
      horarios_consulta: doctor.HorariosConsulta
    });
    setEditDoctor(doctor);
  };

  return (
    <div className="container">
      <div className="form-section">
        <h2>{editDoctor ? "Editar Doctor" : "Registrar Nuevo Doctor"}</h2>
        <form onSubmit={handleSubmit} className="form">
          <label>
            Nombre:
            <input type="text" name="nombre" value={nuevoDoctor.nombre} onChange={handleChange} required />
          </label>
          <label>
            Especialidad:
            <input type="text" name="especialidad" value={nuevoDoctor.especialidad} onChange={handleChange} required />
          </label>
          <label>
            Email:
            <input type="email" name="email" value={nuevoDoctor.email} onChange={handleChange} required />
          </label>
          <label>
            Teléfono:
            <input type="tel" name="telefono" value={nuevoDoctor.telefono} onChange={handleChange} required />
          </label>
          <label>
            Horarios de Consulta:
            <input type="text" name="horarios_consulta" value={nuevoDoctor.horarios_consulta} onChange={handleChange} required />
          </label>
          <button type="submit" className="submit-button">{editDoctor ? "Actualizar" : "Registrar"}</button>
        </form>
      </div>

      <div className="list-section">
        <h1>Lista de Doctores</h1>
        <table className="doctor-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Especialidad</th>
              <th>Email</th>
              <th>Teléfono</th>
              <th>Horarios de Consulta</th>
              <th>Operaciones</th>
            </tr>
          </thead>
          <tbody>
            {doctores.map(doctor => (
              <tr key={doctor.ID_D}>
                <td>{doctor.Nombre}</td>
                <td>{doctor.Especialidad}</td>
                <td>{doctor.Email}</td>
                <td>{doctor.Teléfono}</td>
                <td>{doctor.HorariosConsulta}</td>
                <td>
                  <button className="edit-button" onClick={() => handleEdit(doctor)}>Editar</button>
                  <button className="delete-button" onClick={() => handleDelete(doctor.ID_D)}>Eliminar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
