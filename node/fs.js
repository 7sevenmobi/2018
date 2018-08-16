
const fs = require('fs');
// 为什么读取网络文件会报错 https://nodejs.org/docs/latest-v9.x/api/documentation.json
fs.readFile('e:/github/2018/doss.txt','utf8',function (err,data){
    if(err){
        throw new Error('读取文件失败');
    }else{
        console.log(data);
    }
});