
// eventEmitter对象
// let eventEmitter = require('events').EventEmitter,
//     ee = new eventEmitter();

// // 监听msg事件，并接收emit发射器传递过来的数据
// ee.on('msg',(data)=>{
//     console.log(data);
// });

// // 触发msg事件，并传递数据
// ee.emit('msg','this message was sent by ee.emit')



// 访问douban API
let https = require('https');
let options = {
    host : 'api.douban.com',
    path : '/v2/book/1220562',
    method : 'get'
};

let req = https.request(options,(res)=>{
    res.setEncoding('utf8');
    // 监听 douban API 这个网络事件，一旦有数据传输过来，立即触发此监听器（如果文件数据较多，可能会多次触发）
    res.on('data',(data)=>{
        console.log(JSON.parse(data));
    });
}).end();