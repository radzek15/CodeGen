<template>
  <div class="container py-3">
    <div class="row">
      <div class="col-4">
<!--        <select class="form-select" aria-label="filter-nginx-directives">-->
<!--          <option v-for="i in nginxInstruction" :key="i.id">{{ i.instruction }}</option>-->
<!--          <option v-for="conf in nginxConfiguration" :key="conf.id">{{ conf.name }}</option>-->
<!--        </select>-->
        <h3>Blocks</h3>
        <select class="form-select my-3" multiple aria-label="select-nginx-instruction">
          <option v-for="block in nginxBlocks" :key="block.id" @dblclick="appendToTextArea(`${block.instruction} ${block.argument} {\n\t\n}`)">{{ block.instruction }} {{ block.argument }}</option>
        </select>
        <h3>Directives</h3>
        <select class="form-select my-3" multiple aria-label="select-docker-configuration">
          <option v-for="directive in nginxDirectives" :key="directive.id" @dblclick="appendToTextArea(`${directive.name} ${directive.value}:\n`)">{{ directive.name }} {{ directive.value }}</option>
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
        nginxBlocks: {},
        nginxDirectives: {},
        selectedField: 'Select'
      }
    },
    methods: {
      async fetchNginxBlocks() {
        try {
          const response = await axios.get('http://localhost:8080/api/nginx/instruction/');
          this.nginxBlocks = response.data;
        } catch (error) {
          console.log('Error fetching data:', error);
        }
      },
      async fetchNginxDirectives(){
        try {
          const response = await axios.get('http://localhost:8080/api/nginx/conf/');
          this.nginxDirectives = response.data;
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
      await this.fetchNginxBlocks();
      await this.fetchNginxDirectives();
    }
  }
</script>

<style scoped>

</style>
