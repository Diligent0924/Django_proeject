<template>
  <v-list three-line>
    <h1>자유게시판</h1>
    <br>
    <hr>
    <template v-for="(item, index) in List">
        <!-- <v-list-item-avatar>
          <v-img :src="item.avatar"></v-img>
        </v-list-item-avatar> -->

        <div id="board">
        <v-list-item-content>
          <v-list-item-title v-html="item.title"></v-list-item-title>
          <v-list-item-subtitle v-html="item.content"></v-list-item-subtitle>
        </v-list-item-content>
        </div>
        <hr>
    </template>
  </v-list>
</template>

<script>
import axios from "axios";
export default{
  data() {
    return {
      List : []
    }
  },
  created() {
    var url = 'http://127.0.0.1:8000/Article/';
    axios.get(url)
    .then(response => {
      this.List = response.data; // 세미콜론을 반드시 붙여야함.
      console.log(this.List)
    })
    .catch(
      console.log('Failed')
    )
  }
}
</script>

<style>
  #board{
    margin-top: 2%;
    margin-bottom: 2%;

  }
</style>