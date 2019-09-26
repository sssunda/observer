import React from "react";
import _ from "lodash";
import sc from "styled-components";
import axios from "axios";
import TimeseriesUsageChart from "components/TimeseriesUsageChart";

class TabCPU extends React.Component {
  state = {
    data: [
      {
        x: 'x',
        columns: [
          ['x', '2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04', '2013-01-05', '2013-01-06'],
//            ['x', '20130101', '20130102', '20130103', '20130104', '20130105', '20130106'],
          ['y', 130, 340, 200, 500, 250, 350],
          ['data1', 50, 200, 100, 400, 150, 250],
        ],
        type: "area-spline",
        groups: [['data1', 'y', 'x']],
      }
    ]
  }

  componentDidUpdate() {
    this.updateData();
  }

  updateData = () => {
    let endpoint = process.env.REACT_APP_ENDPOINT;
    if (typeof endpoint == "undefined") {
      console.log("endpoint does not defined")
      return;
    }

    axios.get(endpoint + "/cpu")
      .then(response => {
      });
    console.log(process.env);
  }

  generateDOM() {
    return _.map(this.state.data, function(i) {
      return (
        <TimeseriesUsageChart data={i}/>
      )
    })
  }
  
  render() {
    return (
      <div>
        <button onClick={this.updateData}>Update</button>
        {this.generateDOM()}
      </div>
    )
  }
}

export default TabCPU;