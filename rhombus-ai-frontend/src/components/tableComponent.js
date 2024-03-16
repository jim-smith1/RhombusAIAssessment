import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { UPDATE_URL } from '../constants';

const TableComponent = ({ data }) => {
  const [selectedTypes, setSelectedTypes] = useState({});

  const handleTypeChange = (id, selectedValue) => {
    setSelectedTypes({ [id]: selectedValue });
  };

  useEffect(() => {
    if (Object.keys(selectedTypes).length) {
      axios.patch(`${UPDATE_URL}${Object.keys(selectedTypes)[0]}/patch/`, {
        data_type: Object.values(selectedTypes)[0]
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  }, [selectedTypes])

  return (
    <div className="table-container">
      <h2>Table</h2>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Column Name</th>
            <th>Data Type</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.id}</td>
              <td>{item.column_name}</td>
              <td>
                <select
                  value={selectedTypes[item.id] || item.data_type}
                  onChange={(e) => handleTypeChange(item.id, e.target.value)}
                >
                  <option value="string">String</option>
                  <option value="datetime64[ns]">Datetime</option>
                  <option value="float64">Float</option>
                  <option value="category">Category</option>
                  <option value="object">Text</option>
                </select>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TableComponent;
