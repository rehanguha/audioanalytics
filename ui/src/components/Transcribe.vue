<template>
  <div>
    <h2>Transcribed Text</h2>
    <b-form-textarea v-model="value" :disabled=true debounce="500" rows="3" max-rows="40"></b-form-textarea>
  </div>

</template>

<script>

import axios from 'axios';

export default {
  props: ["selectedFile"],
  data(){
    return {
      value: ''
    }
  },
  mounted(){
    this.get_transcribe_data();
  },
  methods: {
    get_transcribe_data(){
      axios
        .get("http://localhost:5001/transcribe_data?filename=" + this.selectedFile)
        .then(response => {
          this.value = response["data"]["_text"]
        })
        .catch(error => {});      
    }
  }
}
</script>

<style>
 img {
   width: 80%;
 }
 textarea.form-control{
   width: 80%;
   display: inline-block;
 }
</style>