<template>
  <div>
    <h2>Channel Comparison</h2>
    <p>

<table class="table table-bordered table-hover table-fit">
<thead><tr>
  <th>Feature ID</th>
<th>Feature Name</th>
<th >Description</th>
</tr></thead>
<tbody><tr>
<td>1</td>
<td>Zero Crossing Rate</td>
<td>The rate of sign-changes of the signal during the duration of a particular frame.</td>
</tr>
<tr>
<td>2</td>
<td>Energy</td>
<td>The sum of squares of the signal values, normalized by the respective frame length.</td>
</tr>
<tr>
<td>3</td>
<td>Entropy of Energy</td>
<td>The entropy of sub-frames&#39; normalized energies. It can be interpreted as a measure of abrupt changes.</td>
</tr>
<tr>
<td>4</td>
<td>Spectral Centroid</td>
<td>The center of gravity of the spectrum.</td>
</tr>
<tr>
<td>5</td>
<td>Spectral Spread</td>
<td>The second central moment of the spectrum.</td>
</tr>
<tr>
<td>6</td>
<td>Spectral Entropy</td>
<td>Entropy of the normalized spectral energies for a set of sub-frames.</td>
</tr>
<tr>
<td>7</td>
<td>Spectral Flux</td>
<td>The squared difference between the normalized magnitudes of the spectra of the two successive frames.</td>
</tr>
<tr>
<td>8</td>
<td>Spectral Rolloff</td>
<td>The frequency below which 90% of the magnitude distribution of the spectrum is concentrated.</td>
</tr>
<tr>
<td>9-21</td>
<td>MFCCs</td>
<td>Mel Frequency Cepstral Coefficients form a cepstral representation where the frequency bands are not linear but distributed according to the mel-scale.</td>
</tr>
<tr>
<td>22-33</td>
<td>Chroma Vector</td>
<td>A 12-element representation of the spectral energy where the bins represent the 12 equal-tempered pitch classes of western-type music (semitone spacing).</td>
</tr>
<tr>
<td>34</td>
<td>Chroma Deviation</td>
<td>The standard deviation of the 12 chroma coefficients.</td>
</tr>
</tbody></table>
    </p>
    <div class="json-compare">
      <div>
        <json-viewer :value="channel1" boxed :expand-depth=1 copyable ></json-viewer>
      </div>
      <div>
        <json-viewer :value="channel2" boxed :expand-depth=1 copyable></json-viewer>
      </div>
    </div>    
  </div>
</template>

<script>
import JsonViewer from 'vue-json-viewer';
import axios from 'axios';
export default {
  props: ["selectedFile"],
  components: {
    JsonViewer
  },
  mounted(){
    this.get_channel_data();
  },
  data() {
    return {
      channel1: {},
      channel2: {}
    }
  },
  methods: {
    get_channel_data: function(){
          axios
      .get("http://localhost:5001/fe?filename=" + this.selectedFile)
      .then(response => {
        this.channel1 = response["data"]["channel1"];
        this.channel2 = response["data"]["channel2"];
      })
      .catch(error => {});
    }
  }
}
</script>

<style >
  .json-compare{
    display: grid;
    grid-template-columns: 50% 50%;    
  }
  .json-tree-root{
    min-width: 0px !important;
  }
  .jv-container .jv-code.boxed {
    max-height: 500px;
    overflow: auto;
  }
</style>