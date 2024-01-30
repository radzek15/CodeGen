import { createApp } from 'vue'
import { createRouter, createWebHistory } from "vue-router";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import '@fortawesome/fontawesome-free/css/all.css'

import App from './App.vue'
import DockerfileGen from "@/components/Docker/Dockerfile/DockerfileGen.vue";
import DockerComposeGen from "@/components/Docker/DockerCompose/DockerComposeGen.vue";
import NginxGen from "@/components/Nginx/NginxGen.vue";
import HomePage from "@/components/Home/HomePage.vue";

const router = createRouter({
	history: createWebHistory(),
	routes: [
		{ path: '/', component: HomePage},
		{ path: '/docker', component: DockerfileGen },
		{ path: '/docker-compose', component: DockerComposeGen},
		{ path: '/nginx', component: NginxGen}
	],
});

const app = createApp(App);

app.use(router);

app.mount('#app');
