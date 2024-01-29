<template>
  <footer id="footer" class="bg-light text-center">
    <section class='container d-flex justify-content-center justify-content-lg-between p-4 border-bottom'>
      <div class='me-5 d-none d-lg-block'>
        <span>Skontaktuj sie z nami:</span>
      </div>
      <div>
        <a href='https://www.facebook.com/radomir.piatkowski/?locale=pl_PL'
           class='me-3 text-reset'><i class="fa-brands fa-facebook"></i></a>
        <a href='mailto:radzek15@gmail.com'
            class='me-3 text-reset'><i class="fa-brands fa-google"></i></a>
        <a href='https://github.com/radzek15' class='me-3 text-reset'>
          <i class="fa-brands fa-github"></i></a>
        <a href="https://www.linkedin.com/in/radomir-pi%C4%85tkowski-9166a5241/"
           class='me-3 text-reset'><i class="fa-brands fa-linkedin"></i></a>
      </div>
    </section>

    <section class="">
    <div class="container text-center text-md-start mt-5">
      <div class="row mt-3">
        <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">
            <i class="fas fa-gem me-3"></i>CodeGen
          </h6>
          <p>CodeGen is a tool that automates the process of writing code.<br>
            My goal is to transform the world of coding, ensuring it is effortless, enjoyable, and available to all.</p>
        </div>

        <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Code Helpers</h6>
          <p><router-link to="/docker" class="text-reset">Docker</router-link></p>
          <p><router-link to="/docker-compose" class="text-reset">Docker-Compose</router-link></p>
          <p><router-link to="/nginx" class="text-reset">Nginx</router-link></p>
        </div>

        <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Useful links</h6>
          <p><a href="/" class="text-reset">Home</a></p>
          <p><a href="#" class="text-reset">Register</a></p>
          <p><a href="#" class="text-reset">Help</a></p>
        </div>

      </div>
    </div>
  </section>

    <div class='text-center p-3 bg-dark'>
      <p class="text-light mt-3">Copyright: &copy; 2023 CodeGen. All rights reserved.</p>
    </div>
  </footer>
</template>

<script>
  export default {
    name: 'PageFooter',
  }
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>