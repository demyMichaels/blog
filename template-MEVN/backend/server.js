// backend/server.js
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const commentsRoute = require('./routes/comments');

const app = express();

// Middleware
app.use(bodyParser.json());

// Routes
app.use('.comments', commentsRoute);

// Database connection (example, update with your DB connection string)
mongoose.connect('mongodb://localhost:27017/instagram-comments')
  .then(() => console.log('MongoDB connected'))
  .catch(err => console.log(err));

// Start the server
const port = process.env.PORT || 5000;
app.listen(port, () => console.log(`Server running on port ${port}`));
