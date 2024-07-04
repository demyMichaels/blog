// backend/routes/comments.js
const express = require('express');
const axios = require('axios');
const Comment = require('../models/Comment');
const router = express.Router();


router.post('/fetch', async (req, res) => {
    const { postUrl } = req.body;
    try {
        const comments = await fetchInstagramComments(postUrl);
        await Comment.insertMany(comments);
        res.status(200).json({ success: true, comments });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

router.get('/export', async (req, res) => {
    try {
        const comments = await Comment.find();
        // Logic for exporting comments to a file (e.g., CSV)
        res.status(200).json({ success: true, comments });
    } catch (error) {
        res.status(500).json({ success: false, error: error.message });
    }
});

async function fetchInstagramComments(postUrl) {
    // Implement the logic to fetch comments from Instagram using Axios
    // This may involve web scraping or using Instagram's Graph API
    // For simplicity, let's return mock data
    return [
        { username: 'user1', text: 'Great post!', timestamp: new Date(), postId: '12345' },
        { username: 'user2', text: 'Nice!', timestamp: new Date(), postId: '12345' }
    ];
}



// Example route
//router.get('/', (req, res) => {
//  res.send('Comments route');
//});

// Add other routes as needed

module.exports = router;