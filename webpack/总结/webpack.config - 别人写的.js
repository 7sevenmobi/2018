
const path = require('path');
const isDev = process.env.NODEENV === 'development';

const config = {
	target:'web',
	enrty:path.join(dirname, 'src/index.js'),
	output: {
		filename:'bundle.js',
		path: path.join(dirname,'dist')
	},
	//loader配置
	module: {
		rules: [
			{
				test: /.vue$/,
				loader:'vue-loader'
			},
			{
				test: /.css$/,
				use: [
					'style-loader',
					'css.loader'
				]
			},
			{
				test: /.(gif|jpg|jpeg| png|svg)$/,
				use: [
					{
						loader:'url-loader',
						options: {
							limit:1024,
							name: '[name]-xxx.[ext]'
						}
					}
				]
			}
		]
	},
	plugins: [
		new webpack.DedinePlugin({
			'process.env': {
                NODEENV: isDev ? '"development":"production"'
            }
		}),
		new HTMLplugin()
	]
};

if(isDev) {
	// 用来在页面进行js调试
	config.devtool = '#cheap=module-eval-source-map',
	config.devServer = {
		port: 8000,
		//host:'0.0.0.0',
		// 把错误显示在网页上
		overlay: {
			errors: true,
		},
		open: true,
		// 热更新，只改变当前组件的变化，防止其他的信息不见了
		hot: true,
		config.plugins.push(
			new webpack.HotMoudleReplacementPlugin(),
			new webpack.NoEmitOnErrorsPlugin()
		),
		//做路由配置
		//historyFallback: {}
	}
}

module.exports = config;