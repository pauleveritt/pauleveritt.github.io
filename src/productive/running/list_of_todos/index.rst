=============
List of Todos
=============

We aren't really really using any data yet. Let's make a small step in
that direction. Along the way, we'll see other PyCharm ways to execute
code: the Python Console and the Terminal tool.

Steps
=====

#. On the line after defining ``app``, let's add a todo list with two
   todo items in it:

    .. code-block:: python

        todos = [dict(id=1, title='First'), dict(id=2, title='Second')]


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

#. Open PyCharm Preferences with ``Cmd-,``

#. Navigate to ``Build, Execution, Deployment -> Console -> Python Console``
   and look at the options.

#. Click on the "Terminal" tool window button in the bottom of the PyCharm
   window.

#. Activate the Python virtual environment you created during ``New Project``.
   For example:

    .. code-block::

        $ source ~/virtualenvs/epc

#. Do the same 3 lines of Python done above.

#. Click the red ``X`` in the Terminal tool window to close the terminal.

#. Reload your browser and confirm that our data-driven approach works.

Analysis
========

PyCharm has the Run Tool (and as we'll see later, the Debugger Tool) for
executing your project's code. But the interactive prompt is also useful:

- *Python Console*. Get to a Python prompt, in the context of your project.

- *Terminal*. Get to the OS X, Windows, or Linux console prompt, with
  the working directory set to your project root.

Extra Credit
============

#. Can you execute just a selection of ``app.py`` code in the Python Console?

#. ``iPython`` has a great command line interface for interactive Python. Can
   PyCharm's Python Console use it?

#. Is there a way to auto-activate your virtual environment when opening a Terminal?

