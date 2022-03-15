<template>
  <div id="app">
    <p v-if="loading">Loading...</p>
    <ul v-else>
      <li v-for="(value, key) in post" :key="key">
        {{ key }} : {{ value }}
      </li>
    </ul>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      loading: false,
      post: null,
      error: ""
    };
  },
  created: function() {
    this.loading = true;
    axios
      .get("https://jsonplaceholder.typicode.com/posts/1")
      .then(res => {
        this.loading = false;
        this.post = res.data;
      })
      .catch(err => {
        this.loading = false;
        this.error = err;
      });
  }
};
</script>
