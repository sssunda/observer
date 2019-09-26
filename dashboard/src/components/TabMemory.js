import React from "react";
import * as c3 from "c3";
import sc from "styled-components";


class TabMemory extends React.Component {
  state = {
    data: {}
  }

  renderChart() {
  }

  componentDidMount() {
  }

  componentDidUpdate() {
  }

  changeData = () => {
    console.log(process.env.BACKEND_ENDPOINT);
  }
  
  render() {
    return (
      <div>
        <button onClick={this.changeData}>Change</button>
      </div>
    )
  }
}

export default TabMemory;