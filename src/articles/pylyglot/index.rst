============================
Polyglot Python with PyCharm
============================

.. note::

    This series is a work-in-progress.

If you're a long-time Python web developer, you are used to web
technologies. But modern frontend web development might seem alien
and un-Pythonic.

If so, this series of articles is aimed at you. These frontend ideas
are important, but you need a Python guide through the thicket. You
also need a tool that can support your Python *and* frontend development.
PyCharm, with the foundation it shares with WebStorm, is uniquely
suited for this.

In this series we will introduce ideas and packages in isolation,
with hands-on code, screenshots, and more. Each article's code is
`in GitHub
<https://github.com/pauleveritt/pauleveritt.github.io>`_. You can
comment on the articles using Disqus and file bug reportes in the
`issue tracker
<https://github.com/pauleveritt/pauleveritt.github.io/issues>`_.

After each technology is introduced, we also show building a TodoMVC
application from scratch, in the second section below.

Contents
========

.. toctree::
    :maxdepth: 1

    intro
    hello_node/index
    package_json/index
    eslint/index
    npm_run/index
    modules/index
    webpack/index
    chrome_debugging/index
    mocha/index
    es6_imports/index
    pythonic_js/index
    jsdom/index


ToDo MVC Tutorial
=================

Based on the topics covered above in isolation, we put it all together
and write a ToDo application, with a Flask backend and a modern frontend.

.. toctree::
    :maxdepth: 1

    todo_initial/index

- todo_tools
- todo_frontend

- todo_tdd
- todo_commonjs
- todo_webpack
- todo_es6_imports
- todo_pythonic_js