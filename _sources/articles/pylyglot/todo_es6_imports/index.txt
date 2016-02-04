=======================
ES6 Imports for ToDoMVC
=======================

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_es6_imports>`_

As we saw in :doc:`../es6_imports/index`, Babel is a transpiler that opens
the door to Pythonic JS. Let's switch our ToDoMVC codebase over to use
a tiny part: ES6 Modules and imports. Along the way, we'll refactor our
``todo.js`` code a bit.

Steps
=====

#. Install dependencies:

   .. code-block:: bash

        npm install babel-preset-es2015 babel-loader --save-dev

#. Our ``webpack.config.js`` needs to be taught to transpile code using
   Babel when Webpack does its bundling:

   .. literalinclude:: webpack.config.js
        :language: js
        :caption: ToDo webpack.config.js
        :emphasize-lines: 4-11

#. Webpack's use of Babel requires a ``.babelrc`` configuration file:

   .. literalinclude:: .babelrc
        :language: js
        :caption: ToDo .babelrc

#. Our ``.eslintrc`` file needs to be told to lint using ES6 features:

   .. literalinclude:: .eslintrc
        :language: js
        :caption: ToDo .eslintrc
        :emphasize-lines: 9-16

#. The tooling is setup, let's change ``app/todo.js`` to use ES6 imports
   and export a function. Let's also re-organize the code to get rid of
   the ``$(document).ready`` top-level handler:

   .. literalinclude:: app/todo.js
        :language: js
        :caption: ToDo app/todo.js
        :emphasize-lines: 1-2, 4, 57

#. ``app/tmpl.js`` now exports its ``tmpl`` function via an ES6 module
   default:

   .. literalinclude:: app/tmpl.js
        :language: js
        :caption: ToDo app/tmpl.js
        :emphasize-lines: 4

#. Finally, ``app/app.js`` switches to ES6 imports. Plus, it runs the
   function exported by ``todo.js``. Note that we can name this function
   whatever we want on the import side:

   .. literalinclude:: app/app.js
        :language: js
        :caption: ToDo app/app.js
        :emphasize-lines: 1-2, 13

#. *Restart/reload*. Webpack needs to get the new configuration changes
   in ``webpack.config.js``. Restart your ``npm start`` tool window,
   then reload your browser.
