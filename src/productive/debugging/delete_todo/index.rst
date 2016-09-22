===========
Delete Todo
===========

Deleting a todo is an important part of our application. Let's add that
feature while showing more about debugging:

- Run to Cursor

- Evaluate Expression

- Console

- Moving backwards in frames

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/debugging/delete_todo>`_

Steps
=====

This time we're going to reverse our mode of implementation and start
instead with the UI side in ``app.py``.

#. In ``app.py``, change ``list_todos`` to have a delete button:

   .. code-block:: python

    @app.route('/todo/')
    def list_todos():
        todos = Todo.list()
        div = '''<div><a href="/todo/{id}/delete">{title}</a>
        <form method="POST" action="/todo/{id}/delete" style="display: inline">
            <input type="submit" value="x"/>
        </form>
        </div>'''
        form = '''<form method="POST" action="add">
            <input name="todo_id" placeholder="Add todo..."/>
            </form>
        '''
        items = [div.format(id=t.id, title=t.title) for t in todos]
        items.append(form)
        return '\n'.join(items)

#. This form posts to a ``/delete`` route on a todo, so let's add
   that route:

   .. code-block:: python

    @app.route('/todo/<int:todo_id>/delete', methods=['POST'])
    def delete_todo(todo_id):
        todo = Todo.get_id(todo_id)
        return redirect('/todo/')

#. Put a breakpoint on the first line inside this ``delete_todo`` route.
   Reload your browser (restarting your app in the debugger if necessary)
   and click on the ``x`` for one of the todos.

#. When execution stops in the route, confirm that ``todo_id`` is an
   integer.

#. Click ``Resume`` |resume| to continue execution.

#. In ``models.py``, add a method for deletion:

   .. code-block:: python

    def delete(self):
        todos.remove(self)

#. Back in ``app.py``, add a line to ``delete_todo`` that calls this
   new method:

   .. code-block:: python

    @app.route('/todo/<int:todo_id>/delete', methods=['POST'])
    def delete_todo(todo_id):
        todo = Todo.get_id(todo_id)
        todo.delete()
        return redirect('/todo/')

#. Reload browser and click X to delete the *second* todo. Execution
   stops at your breakpoint.

#. Put your cursor in the ``delete`` method in ``models.py``.

#. In the debugger, click ``Run to Cursor`` |runtocursor|.

#. Let's make sure this is the correct todo. Click the
   ``Evaluate Expression`` button |evaluate|.

#. In the popup window, enter ``self.id == 2`` to confirm that this is the
   correct todo. (Note: it might not be ``2`` based on the sorting and random
   title generation.)

#. Click the Debug Tool Window's ``Console`` tab (beside the ``Debugger``
   tab), then click the ``Show Python Prompt`` button |prompt|.

#. Let's see what ``todo_int`` was defined as in the earlier stack frame
   by clicking ``delete_todo`` in the ``Frames`` window. ``Variables``
   updates to show us the new scope.

#. Click the ``Resume`` button |resume|.

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in Delete Todo
    :language: py

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Delete Todo
    :language: py



.. |resume| image:: https://www.jetbrains.com/help/img/idea/debug_resume.png

.. |runtocursor| image:: https://www.jetbrains.com/help/img/idea/frames_run_to_cursor.png

.. |evaluate| image:: https://www.jetbrains.com/help/img/idea/variables_evaluate_expr.png

.. |prompt| image:: https://www.jetbrains.com/help/img/idea/icon_showCommandLine.png