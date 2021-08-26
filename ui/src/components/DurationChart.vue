<template>
  <div>
    <hr>
    <h2>Duration Statistics</h2>
    <p></p>
    <highcharts :options="chartOptions"></highcharts>
    <hr>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import highcharts from "highcharts-vue";
import More from "highcharts/highcharts-more";
import axios from "axios";
More(Highcharts);
export default {
  props: ["selectedFile"],
  mounted() {
    axios
      .get(
        "http://localhost:5001/quantileanalysis?filename=" + this.selectedFile
      )
      .then(response => {
        let data = JSON.parse(response["data"])[0];
        this.chartOptions.series = [
          {
            name: "Speaking Duration",
            data: [parseFloat(data["speaking_duration"]),0,0]
          },
          {
            name: "Original Duration",
            data: [0,parseFloat(data["original_duration"]),0]
          },
        { name: "Balance", data: [0,0,parseFloat(data["balance"])] }
        ];
      })
      .catch(error => {});
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "bar"
        },
        title: {
          text: ""
        },
        xAxis: {
          categories: ['Speaking Duration (SD) (excl. fillers and pause)',
            'Original Duration (OD) (inc. fillers and pause)',
            'Balance (Ratio b/w SD and OD)']
        },
        yAxis: {
          min: 0,
          title: {
            text: "Count"
          },
          stackLabels: {
            enabled: true,
            style: {
              fontWeight: "bold",
              color:
                // theme
                (Highcharts.defaultOptions.title.style &&
                  Highcharts.defaultOptions.title.style.color) ||
                "gray"
            }
          }
        },
        legend: {
          reversed: true
        },
        plotOptions: {
          series: {
            stacking: "normal"
          }
        },
        series: []
      }
    };
  }
};
</script>

<style></style>
