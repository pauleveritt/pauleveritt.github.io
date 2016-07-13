===========
Single Todo
===========

Our ``show_todo`` is still using dummy data. Let's have it use actual data,
with a lookup static method from ``models.Todo`` similar to how we get the
list of todos. As we do this, we'll see how to efficiently re-arrange code.

Steps
=====

#. In ``models.py``, let's start by extending ``populate_todos`` to add
   a total of 3 sample todos. Put your cursor on
   ``todos.append(Todo('First'))`` and press ``Cmd-D`` twice to duplicate
   the line. Changed the next two lines to have an argument of ``'Second'``
   and ``'Third'``.

#. The ``Todo`` class constructor looks weird. ``self.title`` should be
   assigned on the first line. Click anywhere in that line and press
   ``Shift-Alt-Up`` to move the line up.

#. After the ``__init__`` constructor, add a new method:

    .. code-block:: python

        def get_id(self, todo_id):
            return [todo for todo in todos if todo.id == todo_id][0]

#. Hmm, PyCharm thinks something's going on with ``get_id``. Mouse-over it
   and see that it thinks this method can be static. Click on
   ``def get_id``, press ``Alt-Enter``, and change it to a static method.

#. Let's take this for a test drive. Change ``model.py``'s main block:

    .. code-block:: python

        if __name__ == '__main__':
            populate_todos()
            first_todo = Todo.list()[0]
            first_id = first_todo.id
            print(Todo.get_id(first_id))

#. Re-run ``models.py`` (make sure the correct run configuration is selected.)

#. We realize ``get_id`` is probably better under ``list``. With your cursor
   anywhere in ``get_id``, press ``Alt-Up`` until PyCharm's selection extends
   to including the method *and* the ``@staticmethod`` decorator.

#. Press ``Shift-Alt-Down`` until the method moves after ``list``.

#. As usual, press ``Cmd-Alt-L`` to clean up any line formatting.

#. We need our web app to use this method for ``show_todo``. In ``app.py``,
   we're going to add a line ``todo = Todo.get_id(todo_id)``, using
   autocomplete. Type ``todo = T`` then tab, ``.`` and tab to accept
   ``get_id``, then ``t`` and tab to complete ``todo_id``.

#. Let's have a bit richer HTML. On the second line in ``show_todo``,
   define a format string ``fmt = ''``.

#. With your cursor inside that string, press ``Alt-Enter`` and choose
   ``Inject language reference -> HTML``. Now provide this for the value:

    .. code-block:: python

     fmt = '<h1>Todo {todo_id}</h1><p>{{title}}</p>'

   As you type, you'll get the full power of WebStorm HTML editing,
   right in your Python string.

#. Change the third line to use this format string:

    .. code-block:: python

      return fmt.format(todo_id=todo.id, title=todo.title)

#. Reload your browser and go to a todo. You'll get an error in ``get_id``.
   Later we'll use the debugger to hunt down the problem. The reason is, the
   route gives us a string and our id's are integers. Change the route
   definition to ``@app.route('/todo/<int:todo_id>')``.

#. Reload your browser.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Single Todo
    :language: py

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in Single Todo
    :language: py

Analysis
========

PyCharm's productivity features are starting to show:

#. *Moving lines*. ``Shift-Alt-Up`` and ``Shift-Alt-Down`` are so much faster
   then cutting and pasting the line. You don't even have to select anything,
   just click in the line.

#. *Smart autocomplete*. In many places, we get accurate and fast completion.

#. *Language injection*. Having HTML-aware editing, in the middle of Python,
   is quite useful. Same is true for CSS, SQL, JS, etc.

Extra Credit
============

#. We also use ``Shift-Alt-Up`` to move a line up. Can we select an entire
   method and move it, using ``Shift-Alt-Up``?

#. If we extend our selection too far with ``Alt-Up``, will ``Alt-Down``
   gradually de-select?

