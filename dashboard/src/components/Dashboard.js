import React from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import "react-tabs/style/react-tabs.css";

import sc from "styled-components";
import { GlobalHotKeys } from "react-hotkeys";

import TabCPU from "components/TabCPU";
import TabMemory from "components/TabMemory";

const keyMap = {
  TAB_CPU: "1",
  TAB_MEMORY: "2",
}

class Dashboard extends React.Component {
  handlers = {
    TAB_CPU: event => this.setState({ tabIndex: 0 }),
    TAB_MEMORY: event => this.setState({ tabIndex: 1 }),
  }
 
  state = {
    tabIndex: 0,
  }

  render() {
    return (
      <GlobalHotKeys keyMap={keyMap} handlers={this.handlers}>
        <Tabs selectedIndex={this.state.tabIndex} onSelect={tabIndex => this.setState({ tabIndex })}>
          <TabList>
            <Tab>CPU[1]</Tab>
            <Tab>Memory[2]</Tab>
          </TabList>
          <TabPanel key="cpu">
            <TabCPU />
          </TabPanel>
          <TabPanel key="memory">
            <TabMemory />
            </TabPanel>
        </Tabs>
      </GlobalHotKeys>
    )
  }
}

export default Dashboard;