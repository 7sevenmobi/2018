
const fs = require('fs');

let data = 'data for writefile method\n';

// 记录数据到指定文件，如果文件不存在则创建
fs.writeFile('log.txt',data,function(err){
    if(!err){
        console.log('data had been written in log.txt');
    }else{
        throw new Error(err);
    }
});

// 为什么读取网络文件会报错 https://nodejs.org/docs/latest-v9.x/api/documentation.json
fs.readFile('log.txt','utf8',function (err,data){
    if(!err){
        console.log('log.txt: ',data);
    }else{
        throw new Error(err);
    }
});

// shell中设置环境变量（windows环境）
// set AB = 'abfjkdls';

// 读取环境变量
console.log(process.env.MOZ_PLUGIN_PATH);    

