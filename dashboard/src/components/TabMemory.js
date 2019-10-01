import React from "react";
import _ from "lodash";
import sc from "styled-components";
import axios from "axios";
import PanelMemory from "components/PanelMemory";

const TabBody = sc.div`
display: block;
margin: 0 auto;
width: 80%;
`;

class TabCPU extends React.Component {
  state = {
    data: [],
  }

  componentDidMount() {
    this.updateData()
    setInterval(() => this.updateData(), 50000);
  }

  updateData = () => {
    axios.get(process.env.REACT_APP_ENDPOINT + "/memory/server_list")
      .then(response => {
        this.setState({ data: response.data.data });
      });
  }

  generateDOM() {
    return _.map(this.state.data, function(i) {
      return (
        <PanelMemory key={i.server_name} server_ip={i.server_ip} server_name={i.server_name} stored_time={i.stored_time}/>
      )
    })
  }
  
  render() {
    return (
      <TabBody>
        <button onClick={this.updateData}>Update</button>
        {this.generateDOM()}
      </TabBody>
    )
  }
}

export default TabCPU; 