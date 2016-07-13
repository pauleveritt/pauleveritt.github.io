=========
Templates
=========

Generating HTML from Python can be tiresome. Let's put Jinja2 templates
to work in Flask, while showing some PyCharm features such as Emmet
for code completion. For now, though, we'll just convert one view,
the home page, to use a template.

Steps
=====

#. In ``app.py``, let's change the return value of ``home_page`` to
   return a template. Replace that line and instead, type
   ``return render_template`` and press ``Alt-Enter``.

#. Select ``import this name`` and select the first choice, from ``flask``.

#. Finish typing that line, resulting in:

    .. code-block:: python

        @app.route('/')
        def home_page():
            return render_template('index.html', title='Home Page')

#. PyCharm warns us that ``Template file 'index.html' not found. Let's create
   it.

#. Right-click in the Project Tool window on the ``templates`` folder and
   select ``New -> File``. Give it a name of ``index.html`` and click
   ``OK``.

#. Let's use `Emmet <https://www.jetbrains.com/help/pycharm/2016.1/emmet-support.html>`_
   as a way to type fast. In the empty file, type
   ``html>head>title`` and press ``tab``. PyCharm will generate much of the markup,
   leaving your cursor in the ``<title>``.

#. Type ``Todo App: {{ title }}`` and press ``Shift-Enter`` to start a new line.

#. Type ``body>h1`` and press ``tab``. Inside the generated ``<h1>``, enter
   ``{{ title }}`` and press ``Shift-Enter``.

#. Type ``a`` and press tab. With the red box in the ``href``, enter
   ``/todo/`` and press ``enter``. The cursor moves inside the ``<a>``.
   Type ``Todos``.

#. Close the ``index.html`` tab.

#. In ``app.py``, note that the ``index.html`` is no longer a warning. Confirm
   that PyCharm can find the template by clicking in ``'index.html'`` and
   pressing ``Cmd-B``. PyCharm opens ``index.html`` from the ``templates`` folder.

#. Reload your browser on the root URL.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Templates
    :language: py

#. Your ``templates/index.html`` should match the following:

   .. literalinclude:: templates/index.html
    :caption: templates/index.html in Templates
    :language: html

Analysis
========

We added Flask template support, but saw a few last productivity features along
the way:

- *Emmet support*. PyCharm has a number of facilities for generating code. We
  previously saw Live Templates. Emmet is another. Postfix completion is a third
  way.

- *Templates directory*. PyCharm warned us that a file didn't exist in the
  Flask templates directory.

Extra Credit
============

#. How did PyCharm know that ``index.html`` should be, then was, in a folder
   called ``templates``?

#. Besides HTML, where else can you use Emmet in PyCharm?