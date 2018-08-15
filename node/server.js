
// 创建一个server，浏览器访问http://localhost:8080
const http = require('http');

let info = '<h2>node haha</h2>';

const serv = http.createServer(function (req,res){
    res.writeHead(200,{'Content-Type':'text/html'});
    res.end(info);
}).listen(8080);

