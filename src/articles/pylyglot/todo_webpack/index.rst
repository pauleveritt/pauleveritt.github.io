=============================
Bundling ToDoMVC with WebPack
=============================

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_webpack>`_

Steps
=====

- npm install --save-dev webpack webpack-dev-server

- index.html

    - Replace all 3 <script> with bundle.js

- app.js

    - Get rid of IIFE

    - var $ = require('jquery'),
          ToDos = require('./todo');

    - Move tmpl into tmpl.js

- todo.js

    - Get rid of IIFE

    - var $, tmpl at top

- package.json

    - Add script "start": "webpack-dev-server --content-base app/"

- webpack.config.js::

     module.exports = {
        context: __dirname + '/app',
        entry: './app.js',
        devtool: 'source-map'
       };

- Re-arrange to show PyCharm and Chrome side-by-side, make a change, see result