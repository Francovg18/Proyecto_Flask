import React, { useState, useEffect } from 'react';
import './App.css'; // Importa el archivo CSS

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [loginResult, setLoginResult] = useState(null);
  const [candies, setCandies] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  useEffect(() => {
    // Verificar si hay un token de acceso en el almacenamiento local al cargar la página
    const token = localStorage.getItem('access_token');
    if (token) {
      setIsLoggedIn(true); // Si hay un token, establecer isLoggedIn en true
      listCandies(); // Obtener la lista de dulces si el usuario está autenticado
    }
  }, []); // Ejecutar solo una vez al cargar la página

  const handleLogin = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('access_token', data.access_token); // Guardar el token en el almacenamiento local
        setLoginResult('success');
        setIsLoggedIn(true); // Establecer el estado de la sesión como iniciada
        listCandies(); // Obtener la lista de dulces después del inicio de sesión exitoso
      } else {
        setLoginResult('error');
        console.error('Credenciales inválidas');
      }
    } catch (error) {
      setLoginResult('error');
      console.error('Error al iniciar sesión:', error);
    }
  };

  const listCandies = async () => {
    try {
      const token = localStorage.getItem('access_token');
      const response = await fetch('http://localhost:5000/api/candies/list', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      });

      if (response.ok) {
        const candiesData = await response.json();
        console.log('Dulces obtenidos:', candiesData);
        setCandies(candiesData); // Actualizar el estado con la lista de dulces recibida
      } else {
        console.error('Error al obtener los dulces:', response.statusText);
      }
    } catch (error) {
      console.error('Error al obtener los dulces:', error);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token'); // Eliminar el token de acceso del almacenamiento local al cerrar sesión
    setIsLoggedIn(false); // Establecer el estado de la sesión como cerrada
    setCandies([]); // Limpiar la lista de dulces
    console.log('Logout exitoso');
  };

  return (
    <div className="login-container">
      {isLoggedIn ? (
        <>
          <h2 className="login-title">Lista de Dulces</h2>
          <button className="button" onClick={handleLogout}>Logout</button>
          <ul className="candy-list">
            {candies.map(candy => (
              <li key={candy.id} className="candy-item">{candy.brand} <br />origin: {candy.origin}</li>
            ))}
            
          </ul>
        </>
      ) : (
        <>
          <h2 className="login-title">Login</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="input-field"
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="input-field"
          />
          <button className="button" onClick={handleLogin}>Login</button>
          {loginResult === 'success' && <p className="status-message success-message">Login exitoso</p>}
          {loginResult === 'error' && <p className="status-message error-message">Credenciales inválidas. Por favor, inténtalo de nuevo.</p>}
        </>
      )}
    </div>
  );
};

export default Login;
