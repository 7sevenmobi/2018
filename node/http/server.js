
// 创建一个server，浏览器访问http://localhost:8080
const http = require('http');

let info = '<h2>infomation sent by server </h2>';

const serv = http.createServer(function (req,res){

    // 301响应代码，重定向访问地址
    // res.writeHead('301',{'location':'http://www.tmall.com'});

    res.writeHead(200,{'Content-Type':'text/html'});

    res.end(info);
}).listen(8080,'localhost');

