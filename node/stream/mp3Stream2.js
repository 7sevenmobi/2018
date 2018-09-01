
const http = require('http'),
    fs = require('fs');

http.createServer((req,res)=>{

let mp3 = 'http://fs.w.kugou.com/201809011649/20ea38c465511da959885cba8e4db00e/G009/M06/14/13/qYYBAFT92PmAIWeoADhvV-J3hFM633.mp3';
// let stat = fs.statSync(mp3);

let rdata = '';
http.get(mp3,(res)=>{
    res.on('data',(chunk)=>{
        rdata += chunk;
    });
});

res.writeHead(200,{
    'Content-Type':'text/html',
    // 'Content-Length':stat.size
});

res.end(rdata);
// fs.createReadStream(mp3).pipe(res);
}).listen(3000,'localhost');