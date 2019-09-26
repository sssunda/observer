import React from "react";
import PropTypes from "prop-types";
import * as c3 from "c3";



class TimeseriesUsageChart extends React.Component {
  renderChart() {
    c3.generate({
      bindto: "#chart1",
      data: this.props.data,
      axis: {
        x: {
          type: "timeseries",
          tick: {
            format: "%Y-%m-%d %H:%M:%S"
          },
        }
      },
      grid: {
        y: {
          show: true
        }
      }
    });
  }

  componentDidMount() {
    this.renderChart();
  }

  componentDidUpdate() {
    this.renderChart();
  }

  render() {
    return (
      <div>
      <div id="chart1"/>
      </div>
    );
  }
}

TimeseriesUsageChart.propTypes = {
  chart_id: PropTypes.string.isRequired,
  data: PropTypes.object.isRequired,
}

export default TimeseriesUsageChart;