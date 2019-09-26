import React from 'react';
import './App.css';
import "c3/c3.css";
import "react-tabs/style/react-tabs.css";
import NavBar from "components/NavBar"
import Dashboard from "components/Dashboard"


class App extends React.Component {
  componentWillMount() {
    document.title = "Observer";
  }

  render() {
    return (
      <div className="App">
        <header>
        </header>
        <body>
          <NavBar/>
          <Dashboard/>
        </body>
      </div>
    );
  }
}

export default App;
