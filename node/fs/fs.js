
const fs = require('fs');

let data = 'written by fs.writefile in fs.js\n';
        
// 记录数据到指定文件，如果文件不存在则创建
fs.writeFile('log.txt',data,function(err){
    if(!err){
        console.log('data had been written in log.txt');
    }else{
        throw new Error(err);
    }
});

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

