
let fs = require('fs'),
    readStream = fs.ReadStream('sort.txt'),
    writeStream = fs.WriteStream('sort_write.txt');

// readStream.setEncoding('utf8');
// readStream.on('data',(chunk)=>{
//     writeStream.write(chunk);
// });
// readStream.on('close',()=>{
//     writeStream.end('close...');
// });

readStream.pipe(writeStream);