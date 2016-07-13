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
   ``(self, title):``.

#. With the cursor still on the ``e`` in ``title``, press ``Alt-Enter``.

#. Choose ``Add field 'title' to class ToDo`` from the Quick Fix list.

#. With the red box outlining ``.title``, press enter to accept the
   suggested field name and jump to the end of the line.

#. On the next line in the constructor, add ``self.id = randint(1000, 9999)``
   and, when your cursor is after the last ``9``, press ``Shift-Enter`` to
   Start New Line *after the end* of the current line.

#. Click in ``randint``, press ``Alt-Enter``, and choose
   ``Import 'random.randint'``. To move there from the end of the line, you
   can use ``Alt-Left`` to jump by word.

#. As always, ``Cmd-Alt-L`` to clean up formatting.

#. Make a Python representation by starting a new method:

    .. code-block:: python

        def rep

    ...and hit ``tab``. PyCharm will complete the ``__repr__(self):``.

#. Finish the method with
   ``return 'Todo {todo_id}'.format(todo_id=self.id)``.

#. Change ``populate_todos`` to append instances:
   ``todos.append(ToDo('First'))``.

#. Change the ``print`` statement at the bottom to
   ``print(todos)``.

#. Re-run to confirm (``Ctrl-R``).

#. Let's confirm nothing has changed or broken in the browser by
   reloading the URL.

#. Our ``app.py`` needs to get its ``todos`` from ``models.py``
   instead of keeping its own list. Remove the ``todos = `` line
   and add an import at the top:

    .. code-block:: python

      from models import todos

#. ``list_todos`` is using dictionary access. Let's convert it to
   attribute access:

    .. code-block:: python

      items = [div.format(id=t.id, title=t.title) for t in todos]

   *Remember to use autocomplete on ``.format``!*

#. Finally, we need to populate our todos. In the main block at
   the bottom for ``app.py``, start a new line and type
   ``populate_todos``.

#. Before adding parentheses, generate the import by pressing
   ``Alt-Enter`` and choosing the first choice. Then add ``()``.

#. Now reload your browser and you should see your list of one todo.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Todo Class
    :language: py

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in Todo Class
    :language: py

Analysis
========

We did quite a lot in this step, letting PyCharm help us on productivity.

- *Autocomplete*. PyCharm handled a lot of typing for us on ``__init__``
  and ``__repr__``, as well as ``.format``. Even if it isn't a lot of
  characters, it's better to let PyCharm do the completion, to avoid typos
  and add in the parens, self, etc.

- *Refactoring*. The "Add field 'title' to class ToDo" refactoring was
  quite helpful. This happens in constructors and methods often.

- *Generate imports*. It's nice to let PyCharm generate the import just
  by using a symbol. Not only does it generate the import, but it leaves
  your cursor exactly where you left it.

Extra Credit
============

#. If you have to stop your editing and go somewhere to add/fix a line,
   what is a quick way to jump back to where you were at?

#. Does PyCharm have a Code Intention to convert dictionary access
   (``todo['id']``) to attribute access (``todo.id``)?

