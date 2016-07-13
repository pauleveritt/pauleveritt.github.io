==========
Todo Class
==========

We're going to start a ``Todo`` class, to replace each dictionary in our
`todos`` list. We'll let PyCharm help us with this code refactoring,
including changing our ``app.py`` web app to use ``model.todos``.

Steps
=====

#. Near the top, under ``todos = []``, let's define a class. Type
   the following and stop at that point:

    .. code-block:: python

        class ToDo:
            def in

    ...and hit ``tab``. PyCharm will complete the ``__init__(self):``.

   .. note::

     Yes, we said ``ToDo`` instead of ``Todo``. We will come back
     to clean that up later.

#. Left-arrow back into the constructor, after self, and change it to
   ``(self, name):``.

#. With the cursor still on the ``e`` in ``name``, press ``Alt-Enter``.


#. Choose ``Add field 'name' to class ToDo`` from the Quick Fix list.

#. With the red box outlining ``.name``, press enter to accept the
   suggested field name and jump to the end of the line.

#. On the next line in the constructor, add ``self.id = randint(1000, 9999)``
   and, when your cursor is after the last ``9``, press ``Shift-Enter`` to
   Start New Line *after the end* of the current line.

#. Click in ``randint``, press ``Alt-Enter``, and choose
   ``Import 'random.randint'``. To move there from the end of the line, you
   can use ``Alt-Left`` to jump by word.

#. As always, ``Cmd-Alt-L`` to clean up formatting.

#. Make a string representation by starting a new method:

    .. code-block:: python

        def st

    ...and hit ``tab``. PyCharm will complete the ``__str__(self):``.

#. Finish the method with
   ``return 'Todo {todo_id}'.format(todo_id=self.id)``.

#. Change ``populate_todos`` to append instances:
   ``todos.append(ToDo('First'))``.

#. Change the ``print`` statement at the bottom to
   ``print(todos[0])``.

#. Re-run to confirm (``Ctrl-R``).

#. Let's confirm nothing has changed or broken in the browser by
   reloading the URL.

#. Our ``app.py`` needs to get its ``todos`` from ``models.py``
   instead

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in Todo Class
    :language: py


Analysis
========

- *Refactoring*.



Extra Credit
============


Todo Class
==========

- Add from models import ToDo in app.py

- We change our mind on ToDo, refactor rename to Todo

- Show that it changes not just in the one file, but everywhere

- Re-run Ctrl-R
