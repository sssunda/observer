import React from "react";
import * as c3 from "c3";
import sc from "styled-components";


class TabCPU extends React.Component {
  state = {
    data: {}
  }

  renderChart() {
  }

  componentDidMount() {
    this.renderChart();
  }

  componentDidUpdate() {
    this.renderChart();
  }

  changeData = () => {
    console.log(process.env);
  }
  
  render() {
    return (
      <div>
        <button onClick={this.changeData}>Change</button>
      </div>
    )
  }
}

export default TabCPU;