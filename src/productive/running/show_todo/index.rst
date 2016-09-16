=========
Show Todo
=========

We need a route for showing an individual todo. Let's use this as a
chance to show more about running Python code in PyCharm. Namely,
let's look more at PyCharm's Run Configurations.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/running/show_todo>`_
`View video/audio walkthrough <http://www.youtube.com/watch?v=VMD5fLPbzRI>`_

Steps
=====

#. In ``app.py``, let's add a route. On the empty line after the
   ``list_todos`` function, add:

   .. code-block:: python

    @app.route('/todo/<todo_id>')
    def show_todo(todo_id):
        return 'ToDo {todo_id}'.format()

#. Now for the return value. Put the cursor inside the parentheses for
   the ``format()``. Using PyCharm's autocompletion, press ``t`` and
   PyCharm suggests ``todo_id``. Press ``enter`` to accept. Press ``=t``
   then accept ``todo_id`` again.

#. Our route should look like this:

    .. code-block:: python

        @app.route('/todo/<todo_id>')
        def show_todo(todo_id):
            return 'ToDo {todo_id}'.format(todo_id=todo_id)

#. Click ``4. Run`` in the bottom of PyCharm to open the Run Tool
   window. Our Flask application should be running. If not, click
   the green play arrow in the Run Tool's window.

#. In PyCharm's toolbar, near the top, click the green play arrow. We wind
   up with a second Flask application listening on the same port. Can
   PyCharm help us prevent this?

#. In the Run Tool window, close the second tab by right-clicking on it
   and choosing ``Close Tab``.

#. Click ``Run -> Edit Configurations`` to edit the ``epc`` run
   configuration.

#. Near the top right, there is a checkbox for ``Single instance only``.
   Change it to checked and click ``Ok`` to save your changes.

#. Now click the green play arrow in the toolbar again. PyCharm warns us
   that we already have an instance of this run configuration running.

#. One last housekeeping: we need a web link to get to this view. Change
   ``list_todos`` to return a link to a todo page:

    .. code-block:: python

        return 'Todo List <a href="/todo/1">First Todo</a>'

#. Reload our browser and confirm that our 3 routes work ok.

#. Our ``app.py`` file should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Show Todo
    :language: py

Analysis
========

PyCharm doesn't just run Python code. It provides a configurable, managed
way to run your code in a smart output window.

- *Run Configurations*. A list of different configurations for running
  some of your code, including settings.

- *Run Tool Window*.  Like other tools in PyCharm, the Run Tool
  has a window with tabs for each run configuration that is running
  or has been run.

- *Buttons and Shortcuts*. Running, stopping, and re-running can all
  happen from multiple places, including keyboard shortcuts.

  .. note::

    You can get to the list of shortcuts with ``Help -> Keymap Reference``.

We also saw some other smart PyCharm help in action:

- Flask-aware Live Templates speed up common tasks, such as adding a route.

- PyCharm was smart about the Flask route parameter not appearing in the
  view function's signature.

- Code Insight flagged us when we made mistakes.

- Code Completion helped us avoid extra (and error-prone) typing
  via autocomplete.

Extra Credit
============

#. What flavors of run configurations are supported in PyCharm
   Professional?

#. Is there a special run configuration for Flask?

#. How did we get this

#. Can run configurations be shared?

#. Does PyCharm use different configurations for running code versus
   debugging code?

#. How do you clear all the lines of output in the run tool window?

#. Did PyCharm have a Quick Fix for the route string warning?

