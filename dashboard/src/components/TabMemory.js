import React from "react";

import sc from "styled-components";


class TabMemory extends React.Component {
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