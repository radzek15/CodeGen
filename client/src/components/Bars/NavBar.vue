<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container d-flex align-items-center justify-content-between">
      <a class="navbar-brand" href="/"><i class="fa-sharp fa-solid fa-code"></i> CodeGen</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarScroll" aria-controls="navbarScroll" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarScroll">
        <ul class="navbar-nav me-auto my-2 my-lg-0 navbar-nav-scroll" style="--bs-scroll-height: 100px;">
          <li class="nav-item dropdown">
            <a class="nav-link active dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Generators
            </a>
            <ul class="dropdown-menu">
              <li><router-link class="dropdown-item" to="/docker">Docker</router-link></li>
              <li><router-link class="dropdown-item" to="/docker-compose">Docker-compose</router-link></li>
              <li><router-link class="dropdown-item" to="/nginx">Nginx</router-link></li>
<!--              <li><hr class="dropdown-divider"></li>-->
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar',
  }
</script>

<style scoped>

</style>
