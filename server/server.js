var http = require('http');
var fs = require('fs');

var createServerSnippet =  function(req, res) {
  fs.readFile("chat.html", function(err, data ) {
      res.end(data);
  }) ;
}

var app = http.createServer(createServerSnippet).listen(3000);
//console.log("listening localhost:3000");

var io = require('socket.io').listen(app);
io.sockets.on('connection', function(socket) {
    //console.log("socket connected");
    socket.on("msgToClient", function(data) {
        io.sockets.emit("msgFromSever", {message: data.msg})
    })
});
