<template>
  <div>
    <h2>Audio Statistics</h2>
    <p>some discription</p>
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
  name: "RadialChart",
  mounted() {
    axios
      .get("http://localhost:5001/quantileanalysis?filename=c.wav&path=input")
      .then(response => {})
      .catch(error => {});
  },
  data() {
    return {
      chartOptions: {
        colors: ["#FFD700", "#C0C0C0", "#CD7F32"],
        chart: {
          type: "column",
          inverted: true,
          width: 800,
          polar: true
        },
        title: {
          text: ""
        },
        tooltip: {
          outside: true
        },
        pane: {
          size: "85%",
          innerSize: "20%",
          endAngle: 270
        },
        xAxis: {
          tickInterval: 1,
          labels: {
            align: "right",
            useHTML: true,
            allowOverlap: true,
            step: 1,
            y: 3,
            style: {
              fontSize: "13px"
            }
          },
          lineWidth: 0,
          categories: [
            'Stat 1 <span class="f16"><span id="flag" class="flag no">' +
              "</span></span>",
            'Stat 2 <span class="f16"><span id="flag" class="flag us">' +
              "</span></span>",
            'Stat 3 <span class="f16"><span id="flag" class="flag de">' +
              "</span></span>",
            'Stat 4 <span class="f16"><span id="flag" class="flag ca">' +
              "</span></span>",
            "Stat 5 "
          ]
        },
        yAxis: {
          crosshair: {
            enabled: true,
            color: "#333"
          },
          lineWidth: 0,
          tickInterval: 25,
          reversedStacks: false,
          endOnTick: true,
          showLastLabel: true
        },
        plotOptions: {
          column: {
            stacking: "normal",
            borderWidth: 0,
            pointPadding: 0,
            groupPadding: 0.15
          }
        },
        series: [
          {
            name: "Gold medals",
            data: [132, 105, 92, 73, 64]
          },
          {
            name: "Silver medals",
            data: [125, 110, 86, 64, 81]
          },
          {
            name: "Bronze medals",
            data: [111, 90, 60, 62, 87]
          }
        ]
      }
    };
  }
};
</script>

<style></style>
