<template>
  <div id="app">
    <SideNav @selectedTab="selectedTab" :selectedFile="selected_file"></SideNav>
    <Body :selected="selected" @sendFile="sendFile"></Body>
    <!-- <HelloWorld msg="Welcome to Your Vue.js App" /> -->
  </div>
</template>

<script>
import SideNav from "./components/SideNav";
import Body from "./components/Body";
import Upload from "./views/Upload";

import _ from "lodash";
export default {
  name: "App",
  components: {
    SideNav,
    Body,
  },
  data() {
    return {
      selected: {value: "upload"},
      selected_file: ""

    };
  },
  methods: {
    selectedTab: function(selected){
      this.selected = selected;
    },
    sendFile: function(selected){
      this.selected_file = selected;
    }
  }
};
</script>

<style>
.highcharts-container{
  width: 100% !important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: grid;
  grid-template-columns: 15% 85%;
}
</style>
