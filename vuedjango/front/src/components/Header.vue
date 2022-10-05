<template>
  <div id="whole">
    <v-toolbar app>
      <span class="hidden-sm-and-up">
        <v-toolbar-side-icon @click="sidebar = !sidebar">
        </v-toolbar-side-icon>
      </span>
      <v-toolbar-title>
        <router-link to="/" tag="span" style="cursor: pointer">
          {{ appTitle }}
        </router-link>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-xs-only">
        <v-btn
          flat
          v-for="item in menuItems"
          :key="item.title"
          :to="item.path">
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>
  </div>

</template>

<script>
export default {
  name: "App",
  data(){
    return {
      appTitle: 'S-MEET',
      sidebar: false,
      menuItems: [
          { title: '반별게시판', path: '/home'},
          { title: '익명게시판', path: '/home'},
          { title: 'Sign Up', path: '/signup'},
          { title: 'Sign In', path: '/signin'}
     ]
    }
  },
};
</script>
<style> 
#whole{
  margin-bottom: 5%;
}
</style>
