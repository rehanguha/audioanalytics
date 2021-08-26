<template>
  <div class='gauge-chart'>
    <h2>Articulation Rate</h2>
    <p>Articulation rate (AR) is a prosodic feature, defined as a measure of rate of speaking in which all pauses are excluded from the calculation. Although there is a general agreement that AR is not constant but varies throughout speech, our knowledge in this area is still very limited.</p>
    <highcharts :options="options"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import highcharts from "highcharts-vue";
import More from "highcharts/highcharts-more";
import solidgauge from "highcharts/modules/solid-gauge";
import axios from "axios";
solidgauge(Highcharts);
export default {
  name: "GaugeChart",
  props: ["selectedFile"],
  mounted() {
    axios
      .get("http://localhost:5001/quantileanalysis?filename="+ this.selectedFile)
      .then(response => {
        var data = JSON.parse(response.data);
        this.options.series[0].data = [parseFloat(data[0]["articulation_rate"])]
      })
      .catch(error => {});
  },
  data() {
    return {
      options: {
        chart: {
          type: "solidgauge",
        },

        title: null,

        pane: {
          center: ["50%", "85%"],
          size: "140%",
          startAngle: -90,
          endAngle: 90,
          background: {
            backgroundColor:
              Highcharts.defaultOptions.legend.backgroundColor || "#EEE",
            innerRadius: "60%",
            outerRadius: "100%",
            shape: "arc"
          }
        },

        exporting: {
          enabled: false
        },

        tooltip: {
          enabled: false
        },

        // the value axis
        yAxis: {
          stops: [
            [0.1, "#55BF3B"], // green
            [0.5, "#DDDF0D"], // yellow
            [0.9, "#DF5353"] // red
          ],
          lineWidth: 0,
          tickWidth: 0,
          minorTickInterval: null,
          tickAmount: 2,
          title: {
            y: -70
          },
          labels: {
            y: 16
          }
        },

        plotOptions: {
          solidgauge: {
            dataLabels: {
              y: 5,
              borderWidth: 0,
              useHTML: true
            }
          }
        },
        yAxis: {
          min: 0,
          max: 5,
          title: {
            text: "Rate of Speech"
          }
        },

        credits: {
          enabled: false
        },

        series: [
          {
            name: "Speed",
            data: [0],
            dataLabels: {
              format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">syllables/sec</span>' +
                "</div>"
            },
            tooltip: {
              valueSuffix: "syllables/sec"
            }
          }
        ]
      }
    };
  }
};
</script>

<style></style>
