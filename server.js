var express = require('express')
, webapp = express()
, server = require('http').createServer(webapp)
, port = 8080
, spawn = require('child_process').spawn
, bl = require('bl')

server.listen(port);

webapp.set('view engine','pug');
webapp.use(express.static(__dirname + '/public'));
webapp.get('/', function(req,res){
  res.render('index')
  })

webapp.post('/please', function(req,res){
  dataString = '';

  py = spawn('python', ['./accountcreator.py']).stdout.pipe(bl(function(err,data){
    credentials = data.toString().replace('\n','').split(',')
    if(typeof credentials != "undefined"){
      responseBody = {
        "Account": {
         "username": credentials[0],
         "password": credentials[1]
        }
        }
    }
    if(typeof responseBody != "undefined"){
      res.json(responseBody);
    }
  }))


  })
