import React from "react";
import _ from "lodash";
import sc from "styled-components";
import axios from "axios";
import TimeseriesUsageChart from "components/TimeseriesUsageChart";
import PropTypes from "prop-types";

class PanelMemory extends React.Component {
  state = {
    chart_data: {
      x: 'x',
      xFormat: '%Y-%m-%d %H:%M:%S',
      columns: [
        ['x'],
        ['cpu_usage'],
      ],
      type: "area-spline",
      groups: [['x', 'cpu_usage']],
    },
  }

  componentDidMount() {
    axios.get(process.env.REACT_APP_ENDPOINT + "/memory/" + this.props.server_name)
    .then(response => {
      const resp_data = response.data.data;
      console.log(resp_data);

      this.setState({chart_data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(resp_data.timeseries),
          ['cpu_usage'].concat(resp_data.cpu_core_percent),
        ],
        type: "area-spline",
        groups: [['x', 'cpu_usage']],
      }});
    })
  }

  render() {
    return (
      <div>
      {this.props.server_ip}<br/>
      {this.props.server_name}<br/>
      {this.props.stored_time}<br/>
      <TimeseriesUsageChart data={this.state.chart_data} />
      </div>
    )
  }
}

PanelMemory.propTypes = {
  server_ip: PropTypes.string.isRequired,
  server_name: PropTypes.string.isRequired,
  stored_time: PropTypes.string.isRequired,
}

export default PanelMemory;