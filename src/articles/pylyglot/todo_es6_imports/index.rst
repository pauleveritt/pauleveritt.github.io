=======================
ES6 Imports for ToDoMVC
=======================

- npm install babel-preset-es2015 babel-loader --save-dev

- Add to webpack.config.js::

      module: {
            loaders: [
                {
                    test: /\.js$/,
                    loader: 'babel-loader'
                }
            ]
        },

- babel-loader needs a Babel configuration, set it at project level in .babelrc::

    {
      "presets": ["es2015"]
    }

- .eslintrc::

  "ecmaFeatures": {
    "modules": true
  },
  "env": {
    "browser": true,
    "jquery": true,
    "es6": true
  }

- app.js::

    import $ from 'jquery';
    import initToDo from './todo';

        initToDo();


- todo.js::

    import $ from 'jquery';
    import tmpl from './tmpl';



- tmpl.js::

    export default function (str, data) {


- Re-organize todo.js to have an init