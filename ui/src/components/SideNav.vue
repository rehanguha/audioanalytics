/* eslint-disable no-debugger */
<template>
<div>
  <sidebar-menu :menu="menu" :width="'200px'" :hideToggle="true" @item-click="onItemClick" />
</div>
</template>

<script>
import { SidebarMenu } from "vue-sidebar-menu";
import "vue-sidebar-menu/dist/vue-sidebar-menu.css";
import Upload from "./../views/Upload";
import Statistics from "./../views/Statistics";
import _ from "lodash";
export default {
  name: "SideNav",
  props: ["selected", "selectedFile"],
  components: {
    SidebarMenu
  },
  methods: {
    onItemClick: function(event, item) {
      var temp = _.cloneDeep(this.menu);
      _.each(temp, e => (e.class = ""));
      var selected = _.first(_.filter(temp, e => e.value == item.value));
      selected.class = "vsm--link_active vsm--link_exact-active";
      this.menu = temp;
      this.$emit("selectedTab", selected);
    },
  },
  watch: {
    selectedFile: {
      handler(){
        var disabled = (this.selectedFile != '' ? false : true)
        _.each(this.menu, function(element){
          if(element.disabled != undefined){
            element.disabled = disabled;
          }
        })
        this.onItemClick(event, this.menu[2]);
      }
    }
  },
  data() {
    return ({
      menu: [
        {
          header: true,
          title: "AudioAnalytica",
          value: "title",
          hiddenOnCollapse: true
        },
        {
          title: "Upload Audio",
          value: "upload",
          icon: "fa fa-upload",
          class: "vsm--link_active vsm--link_exact-active",
        },
        {
          title: "Text Statistics",
          value: "stats",
          icon: "fa fa-file-text",
          class: "",
          disabled: true
        },
        {
          title: "Audio Statistics",
          value: "analytics",
          icon: "fa fa-bar-chart",
          disabled: true
        },
        {
          title: "Share",
          value: "share",
          icon: "fa fa-share",
          disabled: true

        }
      ]
    });
  }
};
</script>
<style>
.v-sidebar-menu .vsm--header {
  text-transform: unset;
}
.v-sidebar-menu .vsm_expanded {
  max-width: 200px;
}
</style>