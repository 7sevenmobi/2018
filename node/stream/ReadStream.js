
let fs = require('fs'),
    stream = fs.ReadStream('latin.txt');

stream.setEncoding('utf8');

// 可读流监听事件 实际上是 eventEmitter 的一个实例

// 这个是监听 读取文件的过程，而不是读取完文件之后，区别于fs.readFile
// 一旦读取到数据，立即触发监听器，所以，如果读取的文件较大，可能会多次触发监听器
stream.on('data',(chunk)=>{
    console.log('chunk');
});

stream.on('close',()=>{
    console.log('all data is read')
})
