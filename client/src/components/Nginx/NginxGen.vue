<template>
  <div class="container py-3">
    <div class="row">
      <div class="col-4">
<!--        <select class="form-select" aria-label="filter-nginx-directives">-->
<!--          <option v-for="i in nginxInstruction" :key="i.id">{{ i.instruction }}</option>-->
<!--          <option v-for="conf in nginxConfiguration" :key="conf.id">{{ conf.name }}</option>-->
<!--        </select>-->

        <select class="form-select my-3" multiple aria-label="select-docker-command">
          <option v-for="i in nginxInstruction" :key="i.id" @dblclick="appendToTextArea(`${i.instruction} ${i.argument} {\n\t\n}`)">{{ i.instruction }} {{ i.argument }}</option>
          <option v-for="conf in nginxConfiguration" :key="conf.id" @dblclick="appendToTextArea(`${conf.name} ${conf.value}\n`)">{{ conf.name }} {{ conf.value }}</option>
        </select>
      </div>

      <div class="col-8">
        <textarea class="form-control" ref="nginxTextArea" placeholder="Your configuration here" id="nginxTextArea" style="height: 800px"></textarea>
        <label for="nginxTextArea">nginx.conf</label>
      </div>
    </div>
  </div>

</template>

<script>
    import axios from "axios";

    export default {
    name: 'NginxGen',
    data() {
      return {
        nginxInstruction: {},
        nginxConfiguration: {},
        selectedField: 'Select'
      }
    },
    methods: {
      async fetchNginxInstruction() {
        try {
          const response = await axios.get('http://localhost:8080/api/nginx/instruction/');
          this.nginxInstruction = response.data;
        } catch (error) {
          console.log('Error fetching data:', error);
        }
      },
      async fetchNginxConfiguration(){
        try {
          const response = await axios.get('http://localhost:8080/api/nginx/conf/');
          this.nginxConfiguration = response.data;
        } catch (error) {
          console.log('Error fetching data:', error);
        }
      },
      appendToTextArea(text) {
        const textarea = this.$refs.nginxTextArea;
        const textBefore = textarea.value.substring(0, textarea.selectionStart);
        const textAfter = textarea.value.substring(textarea.selectionEnd, textarea.value.length);
        textarea.value = textBefore + text + textAfter;
        textarea.focus();
        textarea.selectionStart = textarea.selectionStart + text.length;
        textarea.selectionEnd = textarea.selectionStart + text.length;
      }
    },
    async mounted() {
      await this.fetchNginxInstruction();
      await this.fetchNginxConfiguration();
    }
  }
</script>

<style scoped>

</style>
