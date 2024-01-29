<template>
  <NavBar />
  <main>
    <router-view />
  </main>
  <Footer vali />
</template>

<script>
import NavBar from "./components/Bars/NavBar.vue";
import Footer from "@/components/Bars/Footer.vue";
export default {
  name: 'App',
  components: {
    Footer,
    NavBar,
  }
}
</script>

<style>
#app {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

main {
  flex: 1;
}

Footer {
  margin-top: auto;
}
</style>
