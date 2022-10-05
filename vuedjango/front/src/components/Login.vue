<template>
    <v-form ref="form" v-model="valid" lazy-validation>  
        <v-container>
            <v-row>
                <v-text-field
                  v-model="email"
                  :rules="emailRules"
                  label="E-mail"
                  required
                ></v-text-field>
            </v-row>
            <v-row>
              <v-text-field
            :rules="passwordrules"
            :type="show3 ? 'text' : 'password'"
            name="input-10-2"
            label="password"
            class="input-group--focused"
          ></v-text-field>
            </v-row>
            
            <v-row>
                <v-col cols="6">
                    <v-btn color="success" class="mr-4" @click="login">
                    로그인
                    </v-btn>
                </v-col>
                <v-col cols="6">
                    <v-btn color="success" class="mr-4" @click="submit">
                    회원가입
                    </v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-form>
  </template>

<script>
import axios from 'axios'
    export default {
      data: () => ({ // input data가 있는 경우에 많이 사용함(form은 data:로 정의되는듯?)
        valid: true,
        email: '',
        emailRules: [
          v => !!v || 'E-mail을 입력하세요',
          v => /.+@.+\..+/.test(v) || 'E-mail 형식이 잘못되었습니다.',
        ],

        show3: false,
        password: '',
        passwordrules: [
          v => !!v || '비밀번호를 입력하세요',
          v => v.length >= 8 || '8글자 이상 입력하세요.',
        ],
      }),

      methods: { // Onclick이나 다른 button의 행동으로 인한 변화되는 로직 정의
        login () {
          console.log(this.name, this.password) // console창에서 확인해본다. this.000은 data:에서 가져오는듯..
          var url = 'http://127.0.0.1:8000/User/'; // 내가 가고자하는 DRF 위치를 의미한다.
          var data = {
            email : this.email,
            password : this.password
          }
          console.log(username, email);
          axios.get(url,{username: username, password: password})
        },

        submit (){
          console.log(this.email, this.password)
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
</style>