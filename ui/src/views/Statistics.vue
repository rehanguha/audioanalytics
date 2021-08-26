<template>
  <div>
    <Transcribe :selectedFile="selected_file"></Transcribe>
    <WordCloud :selectedFile="selected_file"></WordCloud>
    <BoxChart :selectedFile="selected_file"></BoxChart>
    <NumbersChart :selectedFile="selected_file"></NumbersChart>
    <DurationChart :selectedFile="selected_file"></DurationChart>    
    <GaugeChart :selectedFile="selected_file"></GaugeChart>
  </div>
</template>

<script>
import BoxChart from "./../components/BoxChart";
import GaugeChart from "./../components/GaugeChart";
import WordCloud from "./../components/WordCloud";
import NumbersChart from "./../components/NumbersChart";
import DurationChart from "./../components/DurationChart";
import Transcribe from "./../components/Transcribe";


export default {
  name: "Body",
  props: ["selected", 'selected_file'],
  components: {
    BoxChart,
    GaugeChart,
    WordCloud,
    NumbersChart,
    DurationChart,
    Transcribe
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