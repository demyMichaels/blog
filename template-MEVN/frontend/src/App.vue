<template>
    <div id="app">
      <h1>Instagram Comments Downloader</h1>
      <input v-model="postUrl" placeholder="Enter Instagram Post URL" />
      <button @click="fetchComments">Fetch Comments</button>
      <button @click="exportComments">Export Comments</button>
      <div v-if="comments.length">
        <h2>Comments:</h2>
        <ul>
          <li v-for="comment in comments" :key="comment._id">{{ comment.username }}: {{ comment.text }}</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        postUrl: '',
        comments: []
      };
    },
    methods: {
      async fetchComments() {
        try {
          const response = await axios.post('/api/comments/fetch', { postUrl: this.postUrl });
          this.comments = response.data.comments;
        } catch (error) {
          console.error('Error fetching comments:', error);
        }
      },
      async exportComments() {
        try {
          const response = await axios.get('/api/comments/export');
          // Handle the export logic (e.g., download the file)
        } catch (error) {
          console.error('Error exporting comments:', error);
        }
      }
    }
  };
  </script>

  <style>
  /* Add some basic styling */
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    text-align: center;
    margin-top: 60px;
  }
  </style>
  