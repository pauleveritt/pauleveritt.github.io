=========
Show Todo
=========

We need a route for showing an individual todo. Let's use this as a
chance to show more about running Python code in PyCharm. Namely,
let's look more at PyCharm's Run Configurations.

Steps
=====

#. In ``app.py``, let's add a route, with help from PyCharm's Live
   Templates.

#. On the empty line after the ``list_todos`` function,
   type ``Cmd-J route`` and press ``enter``.

#. For the function name (when prompted by the red box), enter
   ``show_todo`` and press ``enter``.

#. The red box moves to the route string. Enter ``/todo/<todo_id>`` and
   press ``enter`` again to move to the end of ``pass`` in the function
   body.

#. Press ``Alt-Backspace`` to delete to the beginning of the word.

#. Enter ``return 'ToDo {todo_id}'.format()`` for now.

#. Note that PyCharm has a warning in ``'/todo/<todo_id>'``. Mouse over
   the warning. It's saying our function is missing a parameter. Smart
   PyCharm!

#. Let's correct that warning on the function, changing the function
   to ``def show_todo(todo_id):``.

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

#. In PyCharm's toolbar, near the top, click the green play arrow. Instead
   of running our application, PyCharm pops up a window warning us that
   it is already running. Why? Dismiss the popup by clicking ``Cancel``
   and let's take a look.

#. Click ``Run -> Edit Configurations`` to edit the ``epc`` run
   configuration.

#. Near the top right, there is a checkbox for ``Single instance only``. It
   is checked. Uncheck it and click ``Ok`` to save your changes.

#. Now click the green play arrow in the toolbar again. A second tab opens
   in the Run Tool's window, and Flask complains that another application is
   listening on that port. *That's* why PyCharm created the run configuration
   with that checkbox set.

#. Let's clean up. First, ``Run -> Edit Configurations`` and check the
   box beside ``Single instance only``, then click ``Ok`` to save.

#. In the Run Tool window, close the second tab by right-clicking on it
   and choosing ``Close Tab``.

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

