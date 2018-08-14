/***
****	package.json文件是项目以及运行环境的描述  
****
****	dependencies字段指项目运行时所依赖的模块；
****	devDependencies字段指定了项目开发时所依赖的模块；	
****	script属性用来配置项目在node环境中的参数（个人理解）

		"scripts": {
    		"test": "echo \"Error: no test specified\" && exit 1",
    		"bundle": "webpack",
    		"server": "webpack-dev-server",
    		"build": "set NODE_ENV=production && webpack --config ./webpack.production.config.js --progress"	//设置开发模式
  		}
****
***/
//引入webpack和node的path模块
const webpack = require("webpack");
const path = require("path");

//已安装。这个插件的作用是依据一个简单的index.tmpl.html模板，生成一个自动引用你打包后的JS文件的新index.html
const htmlPlugin = require("html-webpack-plugin");

//未安装。它允许你在修改组件代码后，自动刷新实时预览修改后的效果。
//const hotModuleReplacement = require("hot-module-replacement");

//压缩JS代码，内置插件无需安装
const uglifyJsPlugin = require("uglifyjs-webpack-plugin");

//分离CSS，将CSS以<link>方式导入
const extractTextPlugin = require('extract-text-webpack-plugin');

//去除文件的缓存
const cleanPlugin = require("clean-webpack-plugin");


module.exports = {
	devtool : "eval-source-map",				//调试工具，基于源文件和打包文件生成（仅做调试，项目上线需要null）
	mode : "development",						//设置开发者模式
	//entry : __dirname+"/app/index.js",		//唯一入口文件
	//entry : ["./app/index.js","./app/login.js"],	//多入口文件，但是打包成一个文件
	entry : {									//多入口文件，打包成多个对应文件
		jq : __dirname+"/app/login.js",		//这里的入口顺序，决定了客户端加载顺序
		index : __dirname+"/app/index.js"
	},
	output : {
		path : path.join(__dirname,"/build"),	//打包后的文件存放的位置，绝对路径
		filename : "[name].js"					//打包后输出对应入口文件的文件名([name]=jq、index)	//如果是唯一入口或者数组写法，需指定文件名
	},
	module : {
		rules:[
			/*	{
					test: /app\/css\/reset\.css$/,
					use: resetCss.extract({
						use: "css-loader"
					})
				},
				{
					test:/\.css$/,
					use:styleCss.extract({
						use:"css-loader"
					})
				}
			*/
				//使用extractTextPlugin将css用link方式引入，就不再需要style-loader
				{
					test:/\.css$/,
					use:extractTextPlugin.extract({
						use:"css-loader"
					})
				}
			
		]
	},
	devServer : {
		open : true,
		contentBase : path.join(__dirname,"/build"),	//本地服务器加载的页面所在的目录
		host : 'localhost',								//默认主机
		port : 8080,									//访问端口
		historyApiFallback : true,						//当使用html5 history api时，强制从404页面跳转到index.html
		inline : true									//实时更新
		//hot : true					//热更新，hotModuleReplacement插件属性
	},
	plugins : [

	//js模块
		new htmlPlugin({
			//title:"7sevenmobi",
			template:__dirname+"/app/index.tmpl.html",
			filename:"index1111.html",					//index.tmpl.html打包后的文件
			chunks:["index","jq"]		//指定打包后的html引用的js模块
		}),
		new htmlPlugin({
			//title:"7sevenmobi",
			template:__dirname+"/app/content.tmpl.html",
			filename:"content1111.html",					//content.tmpl.html打包后的文件
			chunks:["index"]						//指定打包后的html引用的js模块
		}),

	//css模块
		//设置打包后的css的保存路径和文件名
		new extractTextPlugin("css/main.css"),	//new extractTextPlugin("css/[name].css") 打包成默认名index.css

	//其他插件
		//new hotModuleReplacement(),

		//webpack内置插件，无需安装
		new uglifyJsPlugin(),

		new cleanPlugin(["build"])		//简单暴力
		//new cleanPlugin('build/*.*', {
		//	root: __dirname,
		//	verbose: true,
		//	dry: false
		//})
	]
}