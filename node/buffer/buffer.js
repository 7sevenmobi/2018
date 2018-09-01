

// 缓冲区和流一起工作，缓冲区被用于读写流中的数据

// 在node.js中，Buffer对象经常用于  作为接收到的数据的缓冲区，以便让数据在全部接收到之后再使用

// octets：字节数
// allocate：分配
// 创建一个Buffer实例
// 并限制其字节为10个长度（默认值0），内容为'a'，采用utf-8编码
let buffer1 = Buffer.alloc(10,'a','utf8')
let buffer2 = Buffer.alloc(10,'a','utf8')

// 在第3个字节处，将内容替换为 hi
buffer1.write('hi',2)
// <Buffer 61 61 68 69 61 61 61 61 61 61>
console.log(buffer1)
// aahiaaaaaa
console.log(buffer1.toString());

buffer2.write('你好',2);
// <Buffer 61 61 e4 bd a0 e5 a5 bd 61 61>
console.log(buffer2);
// aa你好aa
console.log(buffer2.toString());