========
Add Todo
========

We :doc:`just hooked up <../../productivity/single_todo/index>`
a route to view a single todo. It's natural now to hook up
adding todos, meaning an HTML form element that posts to a
view then re-displays the list of todos.

In this step we introduce running under the debugger:

- Launch a debug session

- Speedup the debugger if not on Windows

- Set a breakpoint to stop execution, resume, and remove the
  breakpoint

Steps
=====

#. In ``models.py``, instead of random ids, let's increment
   the ``id`` by changing the ``Todo`` constructor
   (``__init__``) to:

   .. code-block:: python

     self.id = max([todo.id for todo in todos], default=0) + 1

#. We'd like the models module to be self-contained. Let
   the ``Todo`` class handle adding a todo by adding a static method
   to ``Todo``:

   .. code-block:: python

    @staticmethod
    def add(title):
        todo = Todo(title)
        todos.append(todo)
        return todo

#. Change the ``populate_todos`` function to use the class method
   when adding:

   .. code-block:: python

    def populate_todos():
        Todo.add('First')
        Todo.add('Second')
        Todo.add('Third')

#. Confirm this works by re-running the ``models.py`` run configuration.

#. We now import randint but don't use it. Let's PyCharm fix this by
   clicking the menu item ``Code -> Optimize Imports``.

#. Let's now run our web app under the debugger. Click on ``app`` in
   the ``4. Run`` tool window at the bottom, then click the red square
   to stop the regular run.

#. In the editor for ``app.py``, right-click and choose
   ``Debug models.py``.

   .. note::

    If you are on Mac or Linux, the Debugger window's Console tab will
    say something like::

     warning: Debugger speedups using cython not found. Run '"/Users/pauleveritt/projects/pauleveritt/pauleveritt.github.io/env35/bin/python3.5" "/Applications/PyCharm.app/Contents/helpers/pydev/setup_cython.py" build_ext --inplace' to build.

    If so, click the hyperlink after the ``Run`` to install the Cython
    compiled extensions that speed up the debugger. You only need to do
    that once per installed Python on your system.

#. Reload in the browser. Everything should work normally.

#. In ``app.py``, let's add a route:

   .. code-block:: python

    @app.route('/todo/add')
    def add_todo():
        todo_id = request.form['todo_id']
        if todo_id:
            Todo.add(todo_id)
        return redirect('/todo/')

#. ``request`` and ``redirect`` need to be imported. Click on each and
   do ``Alt-Enter`` to let PyCharm help you generate the import.

#. We need an HTML form that collects and submits the todo title. Change
   ``def list_todos()`` to add this to the HTML:

   .. code-block:: python

    @app.route('/todo/')
    def list_todos():
        todos = Todo.list()
        div = '<div><a href="/todo/{id}">{title}</a></div>'
        form = '''<form method="POST" action="add">
            <input name="todo_id" placeholder="Add todo..."/>
            </form>
        '''
        items = [div.format(id=t.id, title=t.title) for t in todos]
        items.append(form)
        return '\n'.join(items)

#. Let's use the debugger, setting a *breakpoint* to pause execution.
   In ``add_todo``, on the line that performs ``Todo.add``, click in the
   left margin beside the line to create a big red circle, aka a
   breakpoint.

#. In your browser, reload the Todo Listing. Type something in the input
   box and press enter.

#. PyCharm appears, with the debugger stopped on the line of the breakpoint.
   Notice also that the browser thinks it is still loading the page, waiting
   for the server response.

#. Continue execution by clicking, in the ``Debug`` tool window, the green
   ``Resume`` button (it looks like a right arrow.)

#. Let's break on the next line. Click on the red circle to remove the
   first breakpoint, then click in the left margin beside the next line
   (where we return the value) to add a new breakpoint.

#. In the browser, type a new value into the input and press enter.

#. PyCharm appears, stopped on the next line.

#. Note that you did *not* have to restart PyCharm when changing
   debugger information such as breakpoints.

#. Remove this second breakpoint by clicking on the red circle.

#. Continue execution by clicking the green ``Resume`` button |resume|.


Extra Credit
============

#. Should we move the ``todos`` array into the ``Todo`` class as a
   class attribute?

.. |resume| image:: https://www.jetbrains.com/help/img/idea/debug_resume.png
