//step 1: create the HTTP server
//Let's import Node.js's built-in HTTP module, he has access
//to function and classes (materials)for creating HTTP server.
//we plan to only work with one http on this site - so we use
//constant reference. When we say http, he's the only one
//we are referring to.
const http = require('http');
//Step 2: Now let's start the creating of the server
//We need the create server tool
//http.createServer({}).listen()
http.createServer(function(req, res){
    res.writeHead(200, {'Content-type':'text/plain'});
    res.end('This is our first touch of this bare site.\n');
}).listen(7070, '127.0.0.1');

console.log('Server running at http://127.0.0.1:7070/');

