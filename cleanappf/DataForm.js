import React, { useState } from 'react';

const DataForm = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    const response = await fetch('http://localhost:5000/clean', {
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button type="submit">Clean Data</button>
      <p>{message}</p>
    </form>
  );
};

export default DataForm;
