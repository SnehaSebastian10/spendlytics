import { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('Loading...');

  useEffect(() => {
    fetch('http://localhost:5000/')
      .then((response) => response.json())
      .then((data) => setMessage(data.message))
      .catch((error) => setMessage('Error connecting to backend'));
  }, []);

  return (
    <div>
      <h1>Spendlytics</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}

export default App;