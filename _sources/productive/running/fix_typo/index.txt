========
Fix Typo
========

Dang, we put ``ToDo`` in the string response instead of ``Todo``. Let's
fix that, while showing how the Run Tool window makes it easy to jump
to run-time errors.

Steps
=====

#. In ``app.py``, change the ``show_todo`` return value to the following:

    .. code-block:: python

            return 'Todo {todo_id}'.format(todo_id=xxxtodo_id)

#. Close the editor tab for ``app.py``.

#. In your browser, click the links until you click on ``First Todo``,
   which should produce an error.

#. In PyCharm, find the last line in the traceback::

  File "/Users/pauleveritt/projects/pycharm/epc2016/epc_tutorial/app.py", line 18, in show_todo

#. Click on the blue-underlined filename to jump to line 18 in that file.

#. Change ```xxxtodo_id`` to ``todo_id``.

#. Reload the web page.

#. ``app.py`` should now look match this:


#. Our ``app.py`` file should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Fix Typo
    :language: py


Analysis
========

In this short task we saw primarily how the tool window works.

- *Jump to errors*. The Run Tool window helps by providing clickable
  links on exceptions, allowing you to easily jump to the line of an
  error, opening the file if necessary.

Extra Credit
============

#. Can the Run Tool's parsing of output cause problems?

#. If your error is a SyntaxError, or a global name error, what happens?

