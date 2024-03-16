import React, { useState } from 'react';
import axios from 'axios';
import TableComponent from './tableComponent';
import { INFER_URL } from '../constants';
import './fileProcessor.css';

const FileProcessor = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [response, setResponse] = useState(null);

  var formData = new FormData();

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = () => {
    if (selectedFile) {
      formData.append('file', selectedFile);
      axios.post(INFER_URL, formData, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      })
      .then(function (response) {
        console.log(response);
        setResponse(response?.data);
      })
      .catch(function (error) {
        console.log(error);
      });
      console.log("Uploading file:", selectedFile);
      setSelectedFile(null);
    } else {
      alert("Please select a file to upload!");
    }
  };

  return (
    <>
      <div className="file-uploader-container">
        <input type="file" onChange={handleFileChange} className="file-input" />
        <button onClick={handleUpload} className="upload-button">Upload</button>
        {selectedFile && (
          <div className="file-info">
            <p>Selected File:</p>
            <p>{selectedFile.name}</p>
          </div>
        )}
      </div>
      <div>
        {response && (
          <TableComponent data={response}/>
        )}
      </div>
    </>
  );
};

export default FileProcessor;
