// 
const http = require('http');

let urls = ['www.baidu.m','www.taobao.com','www.tmall.com'];

function fetchPage(url){
    let start = new Date();
    // 请求web服务器，获取响应数据
    http.get({host : url},function(res){
        console.log('Got response from: ' + url);
        console.log('Request took: ',new Date() - start,'ms');
    }).on('error',function(e){
        throw new Error(e.message);
    });
}

for(let i=0,len=urls.length;i<len;i++){
    fetchPage(urls[i]);
    // 因为fetchPage会执行异步操作，
    // 所以，下行语句会先于fetchPage将信息打印出来
    // console.log(urls[i]);
}