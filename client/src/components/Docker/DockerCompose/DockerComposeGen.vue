<template>
  <div class="container py-3">
    <div class="row">
      <div class="col-4">
        <select class="form-select" v-model="selectedKey" @change="fetchComposeInstructions" aria-label="filter-compose-instruction">
          <option v-for="i in uniqueInstructions" :key="i">{{ i }}</option>
        </select>

        <select class="form-select my-3" multiple aria-label="select-docker-command">
          <option v-for="i in filteredInstructions" :key="i.id" @dblclick="appendToTextArea(`${i.key}: ${i.value}`)">{{ i.key }}: {{ i.value }}</option>
        </select>
      </div>

      <div class="col-8">
        <textarea class="form-control" ref="composeTextArea" placeholder="Your configuration here" id="composeTextArea" style="height: 800px"></textarea>
        <label for="composeTextArea">docker-compose.yaml</label>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jsYaml from "js-yaml";

export default {
  name: 'DockerComposeGen',
  data() {
    return {
      composeInstructions: [],
      selectedKey: 'Select Instruction'
    }
  },
  computed: {
    uniqueInstructions() {
      return ['Select Instruction', ...new Set(this.composeInstructions.map(i => i.key))];
    },
    filteredInstructions() {
      if (this.selectedKey === 'Select Instruction') {
        return this.composeInstructions;
      } else {
        return this.composeInstructions.filter(i => i.key === this.selectedKey);
      }
    }
  },
  methods: {
    async fetchComposeInstructions() {
      try {
        let url = 'http://localhost:8080/api/dockercompose/instruction';
        if (this.selectedKey && this.selectedKey !== 'Select Instruction') {
          url += `?key=${this.selectedKey}`;
        }
        const response = await axios.get(url);
        const parsedData = jsYaml.load(response.data);
        this.composeInstructions = parsedData;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    appendToTextArea(text) {
      const textarea = this.$refs.composeTextArea;
      const textBefore = textarea.value.substring(0, textarea.selectionStart);
      const textAfter = textarea.value.substring(textarea.selectionEnd, textarea.value.length);
      textarea.value = textBefore + text + '\n\t' + textAfter;
      textarea.focus();
      textarea.selectionStart = textarea.selectionStart + text.length + 2;
      textarea.selectionEnd = textarea.selectionStart + text.length + 2;
    }
  },
  async mounted() {
    await this.fetchComposeInstructions();
  }
}
</script>

<style scoped>
/* Your scoped styles here */
</style>
