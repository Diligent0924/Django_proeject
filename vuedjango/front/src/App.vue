<template>
  <v-app class="main">
    <v-main>
      <Header/>
      <Content/>
    </v-main>
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import Content from './components/Content.vue';

export default {
  name: 'App',

  components: {
    Header,
    Content,
},

  data: () => ({
    
  }),
}
</script>

<style>
</style>