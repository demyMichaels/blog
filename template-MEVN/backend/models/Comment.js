const mongoose = require('mongoose');

const CommentSchema = new mongoose.Schema({
    username: String,
    text: String,
    timestamp: Date,
    postId: String
});

module.exports = mongoose.model('Comment', CommentSchema);
