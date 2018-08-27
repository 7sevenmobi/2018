
let http = require('http'),
    fs = require('fs'),
    userNumber = 0;

let server = http.createServer(function(req,res){
    fs.readFile('./index.html',function(err,data){
        res.writeHead(200,{'Content-Type':'text/html'});
        res.end(data,'utf-8');
    });
}).listen(3000,'localhost');


// socket.io监听 server各种事件
let io = require('socket.io')(server);
io.on('connection',function(socket){

    userNumber++;
    // 监听userCounter事件，并将变量userNumber传递给每个新连接的客户端
    socket.emit('userCounter',{userNumber:userNumber});
    // 监听userCounter事件，并将变量userNumber传递给每个已经连接的客户端
    socket.broadcast.emit('userCounter',{userNumber:userNumber});


    // 通讯信息分发
    socket.on('message',function(data){
        socket.broadcast.emit('pushMessage',data);
    });

    // 监听 断开连接
    socket.on('disconnect',function(){
        userNumber--;
        socket.broadcast.emit('userCounter',{userNumber:userNumber});
    });
});