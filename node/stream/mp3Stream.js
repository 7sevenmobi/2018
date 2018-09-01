
const http = require('http'),
    fs = require('fs');

http.createServer((req,res)=>{
    // 网络文件怎么实现
    // let mp3 = 'http://fs.w.kugou.com/201809011649/20ea38c465511da959885cba8e4db00e/G009/M06/14/13/qYYBAFT92PmAIWeoADhvV-J3hFM633.mp3';
    let mp3 = 'song.mp3';
    let stat = fs.statSync(mp3);

    res.writeHead(200,{
        'Content-Type':'audio/mpeg',
        'Content-Length':stat.size
    });

    fs.createReadStream(mp3).pipe(res);
}).listen(3000,'localhost');