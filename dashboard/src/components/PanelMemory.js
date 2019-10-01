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

        this.setState({
          chart_data: {
            x: 'x',
            xFormat: '%Y-%m-%d %H:%M:%S',
            columns: [
              ['x'].concat(resp_data.timeseries),
              ['free'].concat(resp_data.free_memory),
              ['cached'].concat(resp_data.buffers_cached_memory),
              ['used'].concat(resp_data.used_memory),
            ],
            type: "area-spline",
            groups: [['used', 'cached', 'free']],
          }
        });
      })
  }

  render() {
    return (
      <div>
        IP: {this.props.server_ip}<br />
        Hostname: {this.props.server_name}<br />
        Update timestamp: {this.props.stored_time}<br />
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