module.exports = {
    context: __dirname + '/app',
    entry: './app.js',
    module: {
        loaders: [
            {
                test: /\.js$/,
                loader: 'babel-loader'
            }
        ]
    },
    devtool: 'source-map'
};