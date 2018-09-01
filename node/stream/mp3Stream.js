
const http = require('http'),
    fs = require('fs');

http.createServer((req,res)=>{
    let mp3 = 'song.mp3';
    let stat = fs.statSync(mp3);

    res.writeHead(200,{
        'Content-Type':'audio/mpeg',
        'Content-Length':stat.size
    });

    fs.createReadStream(mp3).pipe(res);
}).listen(3000,'localhost');