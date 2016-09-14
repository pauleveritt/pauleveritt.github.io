=============
List of Todos
=============

We aren't really using any data yet. Let's make a small step in
that direction. Along the way, we'll see other PyCharm ways to execute
code: the Python Console and the Terminal tool.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/running/list_of_todos>`_

Steps
=====

#. On the line after defining ``app``, let's add a todo list with two
   todo items in it:

    .. code-block:: python

        todos = [dict(id=1, title='First'), dict(id=2, title='Second')]

   .. note::

     The code line above extends to the right. Make sure you copy to
     the end of the line.

#. Our ``list_todos`` view needs to take these list entries, convert
   it to a string of HTML, and return it:

    .. code-block:: python

        def list_todos():
            div = '<div><a href="/todo/{id}">{title}</a></div>'
            items = [div.format(id=t['id'], title=t['title']) for t in todos]
            return '\n'.join(items)

#. To see if this works, we could of course just reload it in the browser. Let's
   use interactive Python to poke around. Select ``Tools -> Python Console``.

#. In the ``Python Console`` tool window:

    .. code-block:: python

        from app import todos, list_todos
        todos
        list_todos()

#. Click the red ``X`` in the ``Python Console`` tool window to close the Python Console.

#. Open PyCharm Preferences with ``Ctrl-Alt-S``. (macOS: ``Cmd-,``)

#. Navigate to ``Build, Execution, Deployment -> Console -> Python Console``
   and look at the options, then click ``Cancel`` to dismiss the Preferences
   popup.

#. Open the command line by clicking in the bottom of the screen in ``Terminal``.

#. PyCharm starts you in the project directory. Let's take a look at where
   PyCharm stores its data for the project preferences:

    .. code-block:: bash

        $ ls -l .idea

#. Click the red ``X`` in the Terminal tool window to close the terminal.

#. Reload your browser and confirm that our data-driven approach works.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in List of Todos
    :language: py


Analysis
========

PyCharm has the Run Tool (and as we'll see later, the Debugger Tool) for
executing your project's code. But the interactive prompt is also useful:

- *Python Console*. Get to a Python prompt, in the context of your project.

- *Terminal*. Get to the Windows, macOS, or Linux console prompt, with
  the working directory set to your project root.

Extra Credit
============

#. Can you execute just a selection of ``app.py`` code in the Python Console?

#. ``iPython`` has a great command line interface for interactive Python. Can
   PyCharm's Python Console use it?

#. Is there a way to auto-activate your virtual environment when opening a Terminal?

#. Python extra credit...will Python 3.6 make the ``.format()`` less
   cumbersome? Passing in the keyword arguments is no fun.