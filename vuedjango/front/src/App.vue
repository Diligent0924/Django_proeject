<template>
  <v-app class="main">
    <v-main>
      <v-container>
        <v-row>
          <v-col id="Header_section">
            <Header/>
          </v-col>
        </v-row>
        <v-row id="Nav_section">
          <v-col cols="3" id="Login_Section">
            <Login/>
          </v-col>
          <v-col cols="8" id="Information_Section">
            <Carousels/>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <Calender />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <Content/>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Header from './components/Header.vue'
import Content from './components/Content.vue';
import Login from './components/Login.vue';
import Calender from './components/Calender.vue';
import Carousels from './components/Carousels.vue';

export default {
  name: 'App',

  components: {
    Header,
    Content,
    Login,
    Calender,
    Carousels
},

  data: () => ({
    
  }),
}
</script>

<style>
  .main{
    margin: 2%;
  }

  #Header_section{
    padding: 0px;
  }

  #Nav_section{
    height: 200px;
    margin-bottom: 3%;
  }

  #Login_Section{
    margin-right: 7%;
  }

  #Information_Section{
    background-color: blue;
  }
</style>