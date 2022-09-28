<template>
    <v-form ref="form" v-model="valid" lazy-validation class='form'>
      <v-text-field v-model="name"
        :counter="10"
        :rules="nameRules"
        label="Name"
        required
      ></v-text-field>
  
      <v-text-field
        v-model="email"
        :rules="emailRules"
        label="E-mail"
        required
      ></v-text-field>
  
      <v-select
        v-model="select"
        :items="items"
        :rules="[v => !!v || 'Item is required']"
        label="Item"
        required
      ></v-select>
  
      <v-checkbox
        v-model="checkbox"
        :rules="[v => !!v || 'You must agree to continue!']"
        label="Do you agree?"
        required
      ></v-checkbox>
  
      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="submit"
      >
        회원가입
      </v-btn>

      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="login"
      >
        로그인하기
      </v-btn>
  
      <v-btn
        color="error"
        class="mr-4"
        @click="reset"
      >
        Reset Form
      </v-btn>
    </v-form>
  </template>

<script>
import axios from 'axios'
    export default {
      data: () => ({ // input data가 있는 경우에 많이 사용함(form은 data:로 정의되는듯?)
        valid: true,
        name: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => (v && v.length <= 10) || 'Name must be less than 10 characters',
        ],
        email: '',
        emailRules: [
          v => !!v || 'E-mail is required',
          v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        select: null,
        items: [
          'Item 1',
          'Item 2',
          'Item 3',
          'Item 4',
        ],
        checkbox: false,
      }),

      methods: { // Onclick이나 다른 button의 행동으로 인한 변화되는 로직 정의
        submit () {
          console.log(this.name, this.email) // console창에서 확인해본다. this.000은 data:에서 가져오는듯..
          var url = 'http://127.0.0.1:8000/User/'; // 내가 가고자하는 DRF 위치를 의미한다.
          var data = {
            username : this.name,
            email : this.email
          }
          axios.post(url, data) // post : 데이터를 전송한다.(Data를 추가한다는 의미..)
          .then(function(response){ // 정상적으로 잘 갔다면 POST 값을 console에 넣어준다.
            console.log(response);
          })
          .catch(function(error){
            console.log(error)
          });
        },

        login (){
          console.log(this.name, this.email)
          var url = 'http://127.0.0.1:8000/User/';
          axios.get(url) // url에 있는 json파일 전체를 data:로 가져온다.
          .then(function(response){
            console.log(response)
          })
          .catch(function(error){
            console.log(error)
          })
        },

        reset () {
          this.$refs.form.reset()
        },
      },
    }
  </script>

<style>
.form{
    margin-left: 20%;
    margin-right: 20%;
}
</style>