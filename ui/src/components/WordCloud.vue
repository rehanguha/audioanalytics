<template>
  <div>
    <h2>Word Cloud</h2>
    <p>Word Clouds (also known as wordle, word collage or tag cloud) are visual representations of words that give greater prominence to words that appear more frequently.</p>
    <highcharts :options="options"></highcharts>
  </div>
</template>

<script>
import Highcharts from "highcharts";
import highcharts from "highcharts-vue";
import axios from "axios";
import _ from 'lodash';
import More from "highcharts/highcharts-more";
import wordcloud from "highcharts/modules/wordcloud";
wordcloud(Highcharts);
export default {
  name: "WordCloud",
  props: ["selectedFile"],
  data() {
    return {
      options: {
        chart: {
          width: 800
        },
        accessibility: {
          screenReaderSection: {
            beforeChartFormat:
              "<h5>{chartTitle}</h5>" +
              "<div>{chartSubtitle}</div>" +
              "<div>{chartLongdesc}</div>" +
              "<div>{viewTableButton}</div>"
          }
        },
        series: [
          {
            type: "wordcloud",
            data: [
              {  },
            ],
            name: "Occurrences"
          }
        ],
        title: {
          text: ""
        }
      }
    };
  },
  created(){
    this.get_wordcloud_data();
  },
  methods: {
    get_wordcloud_data(){
      axios
        .get("http://localhost:5001/transcribe_data?filename=" + this.selectedFile)
        .then(response => {
          var data = response.data['word_frequency'];
          var temp = []
          _.each(data, (value, key)=> {
            temp.push({'name': key, 'weight': value})
          })
          this.options.series[0].data = temp;
          Highcharts.redraw();
        })
        .catch(error => {});      
    } 
  }
};
</script>

<style></style>
