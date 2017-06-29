===============
Master Template
===============

We are going to convert some more views to use templates. Along the way,
we are going to introduce PyCharm's debugger.

Steps
=====

#. Stop the Run Tool window's execution by clicking the red square button
   in the Run Tool window.

#. Click on the ``templates`` directory and press ``Ctrl-N`` to make a new
   file named ``layout.html`` in the ``templates`` directory.

#. Use Emmet to fill in the HTML for this directory: ``html>head>title``
   then ``tab``.

#. In the ``<title>`` type in ``Todo: {{ title }}``.

#. Use Emmet for the body. After ``</head>`` type in:
   ``body>h1>a`` then press ``tab``.

#. In the ``<h1>``: ``<a href="/">Home</a></h1>``.

#. Press ``Shift-Enter`` and add:

   .. code-block:: jinja

    <h2>{{ title }}</h2>
    {% block content %}
    {% endblock %}
    </body>

#. Right-click on ``templates/index.html`` and choose
   ``Refactor-Rename`` to change the name to ``home_page.html``.

#. Right-click in the editor tab for ``app.py`` and choose ``Debug``.

#. (OS and Linux) In the Debugger console, click on the link that says::

   warning: Debugger speedups using cython not found. Run
   '"/Users/pauleveritt/virtualenvs/epc/bin/python"
   "/Applications/PyCharm.app/Contents/helpers/pydev/setup_cython.py"
   build_ext --inplace' to build.

#. Reload browser on the root URL.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Master
    :language: py

#. Your ``templates/layout.html`` should match the following:

   .. literalinclude:: templates/layout.html
    :caption: templates/layout.html in Master
    :language: jinja

#. Your ``templates/home_page.html`` should match the following:

   .. literalinclude:: templates/home_page.html
    :caption: templates/home_page.html in Master
    :language: jinja
