============
Productivity
============

We've now seen the basics of the PyCharm UI and how to run Python code
in the PyCharm IDE. Along the way, you saw some of the special ninja
tricks for productive coding in PyCharm.

This section focuses much more on faster, more accurate Python
development by putting PyCharm to work. We'll cover more Live
Templates, Code Intentions, refactorings, language injections, and more.

Tasks
=====


.. toctree::
    :maxdepth: 1

    data_model/index.rst
    todo_dicts/index.rst
    todo_class/index.rst
    list_todos_method/index.rst


Get Single Todo
===============

- Excuse to show moving lines up/down

- Add a ``get_id`` static method, after __init__

- Wire it into main

- Ctrl-R to re-run

- Decide we want it after ``def list``

- Extend selection, then use move lines to move down

- Also, re-arrange assignments in constructor

- Ctrl-R

Web List and Show
=================

- Excuse to show some more warnings

- First, explain the style of use-it-then-quick-fix-import

- Change the main block to call ``populate_todos()``, quick fix
  to generate the import

- In home_page use Language Injection in returned string and
  add ``<a href="/todos/">Todos</a>``

- Re-run in browser to confirm

- Use Cmd-J route to Live Template Flask a route for show_todo

- Put in an error in the route specification, show how PyCharm spots it

- Also, forget to put in the int:todo_id, triggering a problem later

Jinja2 Templates
================

- Excuse to show Emmet and Move Refactoring

-