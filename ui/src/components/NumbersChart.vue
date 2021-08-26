<template>
  <div>
    <hr>
    <h2>Quantitative Analysis</h2>
    <p></p>
    <highcharts :options="chartOptions"></highcharts>
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
      .get("http://localhost:5001/quantileanalysis?filename="+ this.selectedFile)
      .then(response => {
        let data = JSON.parse(response['data'])[0]
        this.chartOptions.series[0]['data'] = [parseInt(data['number_of_syllables']), parseInt(data['number_of_pauses'])]
      })
      .catch(error => {});
  },
  data() {
    return {
      chartOptions: {
        chart: {
          type: "column"
        },
        title: {
          text: ""
        },
        xAxis: {
          categories: ['Number of Syllables', 'Number of Pauses'],
          crosshair: true
        },
        yAxis: {
          min: 0,
          title: {
            text: "Count"
          }
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: [{name: '', data: []}],
        legend: {
          enabled: false,
        }
      }
    };
  }
};
</script>

<style></style>
