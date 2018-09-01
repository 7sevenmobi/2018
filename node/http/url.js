
const url = require('url');

let requestUrl = 'https://www.tmall.com:1234/pathname?query=stringhash';

// 获取主机名称 www.tmall.com
url.parse(requestUrl).hostname

// 获取端口 1234
url.parse(requestUrl).port

// 获取路径 /pathname
url.parse(requestUrl).pathname