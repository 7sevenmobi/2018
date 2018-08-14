
// 创建一个server，浏览器访问http://localhost:3000

let info = '<h2>node haha</h2>';

const http = require('http');

const serv = http.createServer(function (req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    res.end(info);
}).listen(3000);

