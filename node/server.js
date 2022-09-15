const curlconverter = require('curlconverter');
const url = require("url");
const util = require('util');
const querystring = require('querystring');
var http = require('http');

// 创建服务器，使用createServer方法
var server = http.createServer(function (req, res) {
    res.statusCode = 200
    res.setHeader("Access-Control-Allow-Origin", "*");
    //允许的header类型
    res.setHeader("Access-Control-Allow-Headers", "content-type");
    //跨域允许的请求方式
    res.setHeader("Access-Control-Allow-Methods", "DELETE,PUT,POST,GET,OPTIONS");
    if (req.method === 'GET') {
        toGet(req, res);
    } else if (req.method === 'POST') {
        toPost(req, res);
    } else if (req.method === 'OPTIONS') {
        res.end('');
    }
}).listen(3000);

function toGet(req, res) {
    let data = 'GET请求内容：\n' + util.inspect(url.parse(req.url));
    res.end('成功');
    console.log(data);
}

function toPost(req, res) {
    // 定义了一个data变量，用于暂存请求体的信息
    let data = '';
    // 通过req的data事件监听函数，每当接受到请求体的数据，就累加到post变量中
    req.on('data', function (chunk) {
        data += chunk;
    });
    let params = querystring.parse(url.parse(req.url).query)
    // 在end事件触发后，通过querystring.parse将post解析为真正的POST请求格式，然后向客户端返回。
    req.on('end', function () {
        res.end(eval(params['method'])(JSON.parse(data)));
    });
}

//curl转其它代码
function toCurl(data) {
    let language = data['language'];
    let value = data['value'];
    return curlconverter[language](value)
}