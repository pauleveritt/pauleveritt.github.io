============
Productivity
============

- Note that this somewhat follows Getting Started Productivity screencast


Data Models
===========

- Used as an excuse to show Live Templates and Quick Fixes

- Create models.py

- Use Cmd-J main to make a main block with ``populate()`` replacing
  ``pass``

- Alt-Enter to generate ``populate_todos``

- Add global ``todos = []`` and have populate_tpdps ``print(todos)``

- Right-click to run it

- Show the live templates and quick fixes in Preferences

Todo Dicts
==========

- Used as an excuse for more intentions, plus quick documentation

- Change populate_todos to append ``{"id": 1, "name": "First"}``

- Ctrl-R to re-run

- Use intention to change from dict literal to dict constructor

- Add a line in __main__ to join a formatted string representation
  of the list

- Explain autocomplete of .format, with quick documentation

- TODO why does .format external documentation not go to the correct thing?

- Ctrl-R to re-run

- Remind them to run Reformat Code

Todo Class
==========

- Excuse to run some refactorings

- Make class ToDo (yes, should be Todo, will use rename later)

- Use autocomplete to complete __init__

- Use navigation to jump back inside the constructor

- Add ``name`` to constructor, then code intention for ``Add field name to
  class ToDo``

- Assign self.id from random.randint, using PyCharm to generate import

- Make a __str__ with .format from code at bottom and explain PyCharm knows
  special methods like __init__ etc.

- Change code at bottom to .join(str(todo)) for all in list

- Reload browser

- Add from models import ToDo in app.py

- We change our mind on ToDo, refactor rename to Todo

- Show that it changes not just in the one file, but everywhere

- Re-run Ctrl-R

List Todos
==========

- Excuse to show deeper refactorings, plus richer warnings

- Add a class method ``list`` to return the todos, plus refactor the
  string representation

- Add ``def list(self): return todos``

- PyCharm warns that this can be a static method, do the quick fix

- In __str__, Refactor Extract the formatting into another method
  ``display``

- Then, in ``display``, use extend selection to select the string,
  then Extract into a field in the Todo constructor

- Wire into main block

- Ctrl-R


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