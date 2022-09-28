<template>
  <v-app class="main">
    <v-main>
      <Header/>
      <Content/>
      <Example/>
    </v-main>
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import Content from './components/Content.vue';
import axios from 'axios';
import Example from './components/example.vue';

export default {
  name: 'App',

  components: {
    Header,
    Content,
    Example
},

  data: () => ({
    
  }),
}
</script>

<style>
</style>