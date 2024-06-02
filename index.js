// http://blog.modulus.io/nodejs-and-express-static-content

var express = require('express');
var app = express();

// app.use(express.static(__dirname + '/public'));
app.use(express.static(__dirname + '/'));
console.log("process.env.PORT = ", process.env.PORT);
app.listen(process.env.PORT || 3000);