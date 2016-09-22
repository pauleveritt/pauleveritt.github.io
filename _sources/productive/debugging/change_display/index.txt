==============
Change Display
==============

We currently let the route decide what to display in the listing of
todos. We should let the todo be in charge of its formatting, for
consistency across our app.

We will use this change to illustrate the following debugger concepts:

- Watches

- Conditional breakpoints

Steps
=====

#. In ``models.py``, let's change the assigned display format to
   also show the ``id``:

   .. code-block:: python

    self.display_fmt = '{title} (ID: {todo_id})'

#. Let's change the ``display`` property we use to calculate and return
   the display value:

   .. code-block:: python

    @property
    def display(self):
        return self.display_fmt.format(todo_id=self.id, title=self.title)

#. Just to be clean, let's change our ``__repr__`` to use this:

   .. code-block:: python

    def __repr__(self):
        return self.display

#. In ``app.py``, change ``list_todos`` to use ``t.display`` instead of
   ``t.title``:

   .. code-block:: python

    items = [div.format(id=t.id, title=t.display) for t in todos]

#. Using the debugger, we'd like to see the calculated value for
   the last todo. Put the breakpoint in ``models.py`` on this line:

   .. code-block:: python

    return self.display_fmt.format(todo_id=self.id, title=self.title)

#. Click the Debugger's ``Rerun`` button |rerun| then reload the todo
   listing in in the browser.

#. Click ``Resume`` |resume| several times until you get to the fifth
   todo, then use ``Evaluate Expression`` |evaluate| to see the value
   of ``self.display``.

#. Let's make that more efficient using a *watch*, which is a way to
   calculate an expression and show in the debugger's ``Variables`` as
   you move through code.

#. In ``Variables`` panel, click the ``+`` button for ``New Watch``.

#. In the input prompt, type this expression and hit enter:

   .. code-block:: python

    ``self.display_fmt.format(todo_id=self.id, title=self.title)``

#. Click the ``Rerun`` button |rerun| then reload the todo listing in
   in the browser.

#. This time, as you step through to the last todo, the watch shows you the
   calculated value that will be returned.

#. It is still inefficient to step until you reach the todo. Let's make
   a *conditional* breakpoint, which only stops when an expression is true.

#. Right-click on your breakpoint inside ``def display``. In the ``Condition``
   box, enter ``self.id == 4``.

#. Click the ``Rerun`` button |rerun| then reload the todo listing in
   in the browser.

#. Note that the debugger this time stops only at the 4th todo.

.. |resume| image:: https://www.jetbrains.com/help/img/idea/debug_resume.png

.. |evaluate| image:: https://www.jetbrains.com/help/img/idea/variables_evaluate_expr.png

.. |rerun| image:: https://www.jetbrains.com/help/img/idea/rerunConsole.png

