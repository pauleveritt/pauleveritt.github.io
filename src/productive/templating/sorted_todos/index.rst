=====================
Sorted Todos Template
=====================

We're returning a list of todos, but they aren't sorted. Let's
add that, and also show debugging in Python code, instead of
just template code.

Steps
=====

#.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in Sorted Todos
    :language: py

#. Your ``templates/list_todos.html`` should match the following:

   .. literalinclude:: templates/list_todos.html
    :caption: templates/list_todos.html in Sorted Todos
    :language: jinja

#. Your ``templates/show_todo.html`` should match the following:

   .. literalinclude:: templates/show_todo.html
    :caption: templates/list_todos.html in Sorted Todos
    :language: jinja


Sorted Listings
===============

- Back in models.py, we're going to change ``def list`` to return
  a sorted listing

- First, right-click Debug to run it under the debugger

- Then, refactor to extract the return value into a local variable

- Change to assign a sorted list to that variable

- Set a breakpoint on the assignment

- Ctrl-D and confirm

