/***
****	package.json文件是项目以及运行环境的描述，其中的script属性用来配置项目在node环境中的参数（个人理解）  
****
		"scripts": {
    		"test": "echo \"Error: no test specified\" && exit 1",
    		"bundle": "webpack",
    		"server": "webpack-dev-server",
    		"build": "set NODE_ENV=production && webpack --config ./webpack.production.config.js --progress"	//设置开发模式
  		}
****
***/

const webpack = require("webpack");
const path = require("path");			//引入node的path模块

/***	内置插件无需install		***/

const htmlPlugin = require("html-webpack-plugin");	//已安装。这个插件的作用是依据一个简单的index.tmpl.html模板，生成一个自动引用你打包后的JS文件的新index.html
//const hotModuleReplacement = require("hot-module-replacement");		//未安装。它允许你在修改组件代码后，自动刷新实时预览修改后的效果。
const uglifyJsPlugin = require("uglifyjs-webpack-plugin");		//压缩JS代码，内置插件
const extractTextPlugin = require('extract-text-webpack-plugin');	//分离CSS，将CSS以<link>方式导入
const cleanPlugin = require("clean-webpack-plugin");	//去除文件的缓存

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
				{
					test:/\.css$/,		//解析css

				//	use:["style-loader","css-loader"]	//从右向左解析
				//	也可以这样写，这种方式方便写一些配置参数	
				//	use:[
				//		{"loader":"style-loader"},
				//		{"loader":"css-loader"}
				//	]
				//	将css格式文件用link方式引入，就不再需要style-loader
					use:extractTextPlugin.extract({
						use:"css-loader"
					})
				}
		]
	},
	devServer : {
		open : true,
		contentBase : path.join(__dirname,"/build"),	//本地服务器加载的页面所在的目录
		//host : '0.0.0.0',								//主机IP
		port : 8080,									//访问端口
		historyApiFallback : true,						//当使用html5 history api时，强制从404页面跳转到index.html
		inline : true									//实时更新
		//hot : true					//热更新，hotModuleReplacement插件属性
	},
	plugins : [							//为每个html页面配置需要引入的js模块
		new htmlPlugin({
			//title:"7sevenmobi",
			template:__dirname+"/app/index.tmpl.html",
			filename:"index1111.html",					//index.tmpl.html打包后的文件
			chunks:["jq","index"]						//指定打包后的html引用的js模块
		}),
		new htmlPlugin({
			//title:"7sevenmobi",
			template:__dirname+"/app/content.tmpl.html",
			filename:"content1111.html",					//content.tmpl.html打包后的文件
			chunks:["index"]						//指定打包后的html引用的js模块
		}),

		//new hotModuleReplacement(),

		new uglifyJsPlugin(),	//webpack内置插件，无需安装

		//设置打包后的css文件保存路径和文件名
		new extractTextPlugin("css/style.css"),

		//new cleanPlugin(["build"])		//简单暴力
		//new cleanPlugin('build/*.*', {
		//	root: __dirname,
		//	verbose: true,
		//	dry: false
		//})
	]
}