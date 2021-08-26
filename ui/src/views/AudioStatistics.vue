



<template>
  <div>
    <Waveform :selectedFile="selected_file"></Waveform>
    <JsonCompare :selectedFile="selected_file"></JsonCompare>
  </div>
</template>

<script>
import Waveform from "./../components/Waveform";
import JsonCompare from "./../components/JsonCompare";

export default {
  name: "Body",
  props: ["selected", 'selected_file'],
  components: {
    Waveform,
    JsonCompare
  },
  watch: {
    selected: {
      immediate: true,
      handler() {}
    }
  }
};
</script>

<style>
</style>