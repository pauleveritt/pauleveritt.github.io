===================
List Todos Template
===================

We'll convert another view to use a view template with a master template.
In the process, we'll get our first real use of the debugger by setting
a breakpoint in the template.

Steps
=====

#. Let's make a template in ``templates/list_todos.html``:

   .. literalinclude:: templates/list_todos.html
    :caption: templates/list_todos.html in List Todos Templates
    :language: jinja

#. In ``app.py``, change the ``list_todos``, making it much simpler:
   it just hands data to the template:

    .. code-block:: python

        def list_todos():
            todos = Todo.list()
            return render_template('list_todos.html', page_title='List Todos', todos=todos)

   *Note: The page_title mistake is intentional.*

#. Next, let's do the same for ``show_todo``. First, create
   ``templates/show_todo.html``:

   .. literalinclude:: templates/show_todo.html
    :caption: templates/show_todo.html in List Todos Templates
    :language: jinja

#. In ``app.py``, change the ``show_todo``, also making it much simpler:
   it just hands data to the template:

    .. code-block:: python

        def show_todo(todo_id):
            todo = Todo.get_id(todo_id)
            return render_template('show_todo.html', title='Todo ' + str(todo_id), todo=todo)

   *Note: PyCharm Professional autocompletes the template filename from the
   ``templates`` directory, which is very helpful.*

#. In your browser, visit the ``List Todos`` page. We aren't getting a
   ``title`` displayed. Let's debug it.

#. Open ``templates/layout.html`` and click in the left margin on the second
   line, where ``<head><title>`` occurs. Your click should create a red
   circle for a "breakpoint".

#. Reload your browser. PyCharm switches back in view, with the execution
   "stopped" on that line.

#. Look in the "Variables" window at the bottom. You see all the Python
   values defined at that point in the template. You realize ``title``
   isn't there, but ``page_title`` is, thus your error.

#. In the Debug Tool window, click the green arrow play button to
   "Resume Program".

#. In ``app.py``, change ``page_title`` to ``title``.

#. Reload the browser and execution again stops in that place. Confirm
   that a ``title`` variable exists and click the green arrow again
   to Resume Program.

#. Now, the browser provides the List Todos heading.

#. Click the red circle to clear the breakpoint.

#. Let's set a breakpoint in the loop. In ``list_todos.html``, click
   in the left margin on the ``<a>`` in the ``<li>``.

#. Reload the browser. When execution stops, in the ``Variables``
   pane, note that ``todo`` is defined. Expand it to see what
   information it contains.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in List Todos
    :language: py

#. Your ``templates/list_todos.html`` should match the following:

   .. literalinclude:: templates/list_todos.html
    :caption: templates/list_todos.html in List Todos Templates
    :language: jinja

#. Your ``templates/show_todo.html`` should match the following:

   .. literalinclude:: templates/show_todo.html
    :caption: templates/list_todos.html in List Todos Templates
    :language: jinja

