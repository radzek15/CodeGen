<template>
  <div class="container">
    <div class="row">
      <h1 class="text-center p-5 display-1 fw-bold text-dark"> { Code Generator }</h1>
      <p class="text-justify display-6">CodeGen is a tool that automates the process of writing code to make it easier
        for anyone</p>
    </div>
    <div class="row text-center my-3">
      <h1 class="p-5 text-dark fw-bold">Tools</h1>
      <p><router-link to="/docker">Docker</router-link></p>
      <p><router-link to="/docker-compose">Docker-Compose</router-link></p>
      <p><router-link to="/nginx">Nginx</router-link></p>
    </div>

    <div class="row text-center my-3">
      <p>Didn't find the right tool for the job?
        <a href='mailto:radzek15@gmail.com'>Propose a tool</a></p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage"
}
</script>

<style scoped>
  a {
    text-decoration: none;
    color: var(--bs-primary);
  }
</style>