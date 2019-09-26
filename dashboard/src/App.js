import React from 'react';
import './App.css';
import "react-tabs/style/react-tabs.css";
import NavBar from "components/NavBar"
import Dashboard from "components/Dashboard"


function App() {
  return (
    <div className="App">
      <NavBar/>
      <Dashboard/>
    </div>
  );
}

export default App;
