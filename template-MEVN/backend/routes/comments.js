// backend/routes/comments.js
const express = require('express');
const router = express.Router();

// Example route
router.get('/', (req, res) => {
  res.send('Comments route');
});

// Add other routes as needed

module.exports = router;