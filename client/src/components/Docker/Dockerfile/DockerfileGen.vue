<template>
  <div class="container py-3">
    <div class="row">
      <div class="col-4">
        <select class="form-select" v-model="selectedCommand" @change="fetchDockerCommands" aria-label="filter-docker-command">
          <option v-for="command in uniqueInstructions" :key="command">{{ command }}</option>
        </select>
        <select class="form-select my-3" multiple aria-label="select-docker-command">
          <option v-for="command in filteredCommands" :key="command.id" @dblclick="appendToTextArea(`${command.instruction} ${command.argument}`)">
            {{ command.instruction }} {{ command.argument }}
          </option>
        </select>
      </div>
      <div class="col-8">
        <textarea class="form-control" ref="dockerfileTextArea" placeholder="Your configuration here" id="DockerfileTextArea" style="height: 800px"></textarea>
        <label for="DockerfileTextArea">Dockerfile</label>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: 'DockerfileGen',
  data() {
    return {
      dockerCommands: [],
      selectedCommand: 'Select command',
    };
  },
  computed: {
    uniqueInstructions() {
      return ['Select command', ...new Set(this.dockerCommands.map(command => command.instruction))];
    },
    filteredCommands() {
      if (this.selectedCommand === 'Select command') {
        return this.dockerCommands;
      } else {
        return this.dockerCommands.filter(command => command.instruction === this.selectedCommand);
      }
    }
  },
  methods: {
    async fetchDockerCommands() {
      try {
        let url = 'http://localhost:8080/api/dockerfile/command/';
        if (this.selectedCommand && this.selectedCommand !== 'Select command') {
          url += `?instruction=${this.selectedCommand}`;
        }
        const response = await axios.get(url);
        this.dockerCommands = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    appendToTextArea(text) {
      const textarea = this.$refs.dockerfileTextArea;
      const textBefore = textarea.value.substring(0, textarea.selectionStart);
      const textAfter = textarea.value.substring(textarea.selectionEnd, textarea.value.length);
      textarea.value = textBefore + text + '\n\n' + textAfter;
      textarea.focus();
      textarea.selectionStart = textarea.selectionStart + text.length + 2;
      textarea.selectionEnd = textarea.selectionStart + text.length + 2;
    }
  },
  async mounted() {
    await this.fetchDockerCommands();
  }
};
</script>

<style scoped>
/* Your scoped styles here */
</style>
