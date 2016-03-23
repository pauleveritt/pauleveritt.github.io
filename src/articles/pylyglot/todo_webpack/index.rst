=============================
Bundling ToDoMVC with WebPack
=============================

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_webpack>`_

We now have the frontend moved out of the back end, served by a static
web server at a different URL. Great! Let's use :doc:`Webpack <../webpack/index>`
to bundle our JavaScript and run under its development server, giving
us hands-free browser reloading.

Webpack gives us browser-side module loading, so we'll switch ``app.js`` and
``todo.js`` to use CommonJS modules.

Steps
=====

#. From the previous step, make a virtual env if necessary, then install if
   needed the npm and Python dependencies.

#. Hook up ``ESLint`` in preferences if necessary.

#. Install our *new* dependencies:

   .. code-block:: bash

        npm install --save-dev webpack webpack-dev-server

#. Update our HTML file, replacing ``<script>`` nodes for ``jquery.js``,
   ``app.js``, and ``todo.js`` with a single ``bundle.js``:

   .. literalinclude:: app/index.html
        :language: html
        :caption: ToDo Webpack index.html

#. ``tmpl.js`` simply moves the template code out of ``app.js``,
   into an export:

   .. literalinclude:: app/tmpl.js
        :language: js
        :caption: ToDo Webpack tmpl.js

#. ``app.js`` gets rid of the IIFE, imports jQuery, and imports
   ``todo.js``:

   .. literalinclude:: app/app.js
        :language: js
        :caption: ToDo Webpack app.js
        :emphasize-lines: 1-2

#. ``todo.js`` also gets rid of the IIFE. It does *not* do
   ``module.exports``, which seems kind of weird. But that's
   because it does its work on jQuery ``$(document).ready`` and
   we don't want to refactor too much in this step. It does,
   though, import ``jQuery`` and ``tmpl.js`` at the top:

   .. literalinclude:: app/todo.js
        :language: js
        :caption: ToDo Webpack todo.js
        :emphasize-lines: 1-2

#. Let's add a line to ``package.json``'s section for ``scripts``,
   to start the dev server, based in ``app/``:

   .. literalinclude:: package.json
        :language: js
        :caption: ToDo Webpack package.json
        :emphasize-lines: 11

#. We need a (simple) ``webpack.config.js`` to drive the dev server:

   .. literalinclude:: webpack.config.js
        :language: js
        :caption: ToDo Webpack webpack.config.js

#. *Start Flask*. Right-click on ``run_server.py`` and run it.

#. *Run dev server*. Use PyCharm's ``npm run`` too window to run ``start``,
   then visit ``http://localhost:5000/``.

And now we're in business! To emphasize the workflow, let's resize
PyCharm and Chrome so they can be side-by-side. As you type,
you will see the updates automatically.
