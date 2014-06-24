/**
* Module dependencies
*/
var express = require('express')	
	, http = require('http');

var app = express();
var server = app.listen(8086);
var io = require('socket.io').listen(server);

// Clients list
clients = {};

// Connect to app
io.sockets.on('connect', function(socket){	
	socket.on('register', function(data){
		clients[data.process_id] = socket;		
	});
});

// Request process.
app.get('/resultclient/:process_id', function(req, res) {
	var client = clients[req.params.process_id];	
	client.emit('result_process', {successful: 1, msg: "El proceso ha finalizado"});
	res.send("successful");
})

// Send client html.
app.get('/', function(req, res) {
    res.sendfile(__dirname + '/client.html')
})