<template>
  <div>
    <hr>
    <h2>Quantile Analysis (using Box-Plot)</h2>
    <p>Measure fundamental frequency distribution.</p>
    <highcharts :options="options"></highcharts>
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
  name: "BoxChart",
  mounted() {
    axios
      .get("http://localhost:5001/quantileanalysis?filename=" + this.selectedFile)
      .then(response => {
        var data = JSON.parse(response.data)[0];

        var temp = [
          [
            parseFloat(data["f0_min"]),
            parseFloat(data["f0_quantile25"]),
            parseFloat(data["f0_median"]),
            parseFloat(data["f0_quan75"]),
            parseFloat(data["f0_max"])
          ]
        ];
        this.options.series[0]["data"] = temp;
        Highcharts.redraw();
      })
      .catch(error => {});
  },
  data() {
    return {
      options: {
        chart: {
          type: "boxplot",
          width: 800
        },

        title: {
          text: ""
        },

        legend: {
          enabled: false
        },

        xAxis: {
          categories: [""],
          title: {
            text: ""
          }
        },

        yAxis: {
          title: {
            text: "Observations"
          },
          plotLines: [
            {
              value: 932,
              color: "red",
              width: 1,
              label: {
                text: "Theoretical mean: 932",
                align: "center",
                style: {
                  color: "gray"
                }
              }
            }
          ]
        },

        series: [
          {
            name: "Observations",
            data: [],
            tooltip: {
              headerFormat: "<em>Experiment No {point.key}</em><br/>"
            }
          }
        ]
      }
    };
  }
};
</script>

<style>
.highcharts-container {
  width: 100%;
  display: inline-block;
  text-align: center !important;
}
</style>
