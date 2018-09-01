
// 退出码为0，表示成功执行退出
// 退出码为1，表示执行退出失败
// 每个进程都有一个唯一的pid，由操作系统分配
// process.on('exit',(code)=>{
//     console.log(`退出码：${code}，pid：${process.pid}`);
// });


// // 防止程序在初始化从stdin读取时退出
// process.stdin.resume();
// // SIGINT 是发出中断程序信号事件的缩写
// // SIGTERM 和SIGINT功能相同，只是是针对linux和macos系统
// process.on('SIGINT',()=>{
//     console.log('got a SIGINT signal');
//     process.exit(0);
// });


// 创建子进程的两种方法：spawn、fork
let spawn = require('child_process').spawn,
    ping = spawn('ping',['www.tmall.com']);

ping.stdout.setEncoding('utf-8');
ping.stdout.on('data',(data)=>{
    console.log(data);
});