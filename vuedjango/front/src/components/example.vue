<template>
    <div>
         <v-btn color="primary" @click="fetchData">get data</v-btn>
    </div>
</template>

<script>

//axios 라이브러리 import
import axios from 'axios'

export default {
    name: 'example',

    data() {
        return {
           
        };
    },

    mounted() {
       
    },

    methods: {
        fetchData: function() {
            axios.get('https://jsonplaceholder.typicode.com/users/')
            .then(function(response) {
            console.log(response);
            })
            .catch(function(error) {
            console.log(error);
            });
        },
    },
};
</script>

<style lang="scss" scoped>

</style>