import React, { useState } from 'react';
import axios from 'axios';
import "./App.css"

const App = () => {
  const [selectedItems, setSelectedItems] = useState('');
  const [total, setTotal] = useState(0);

  const handleInputChange = (event) => {
    setSelectedItems(event.target.value.toUpperCase());
  };

  const postCheckout = () => {
    axios
      .post('http://127.0.0.1:8000/api/v1/checkout/', { items: selectedItems })
      .then((response) => {
        setTotal(response.data.total);
      })
      .catch((error) => {
        console.error('Error calculating total:', error);
      });
  };

  return (
    <div className="App">
      <h1>Supermarket Checkout</h1>
      <div>
        <label htmlFor="items-input">Enter items: </label>
        <input
          id="items-input"
          type="text"
          value={selectedItems}
          onChange={handleInputChange}
          placeholder="Enter items like AABBC"
        />
      </div>

      <button onClick={postCheckout}>Calculate Total</button>

      <div>
        <h3>Selected Items: {selectedItems}</h3>
      </div>

      <div>
        <h3>Total Price: Rs {total}</h3>
      </div>
    </div>
  );
};

export default App;
