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
   assigned on the first line. Click

#. The constructor looks funny... ``self.title`` should be on the first line.
   Click on that line and press ``Shift-Alt-Up`` to move the line up.



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


Extra Credit
============


#. We also use ``Shift-Alt-Up`` to move a line up. Can we select an entire
   method and move it, using ``Shift-Alt-Up``?



Get Single Todo
===============

- Excuse to show moving lines up/down

- Add a ``get_id`` static method, after __init__

- Wire it into main

- Have populate provide more sample todos

- Ctrl-R to re-run

- Decide we want it after ``def list``

- Extend selection, then use move lines to move down

- Also, re-arrange assignments in constructor

- Ctrl-R

