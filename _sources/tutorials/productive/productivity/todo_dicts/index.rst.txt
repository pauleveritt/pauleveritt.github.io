==========
Todo Dicts
==========

We don't have any todo items to show. Let's use some handy PyCharm
machinery as we implement this: more Code Intentions, Quick Documentation,
and Reformat Code.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/productivity/todo_dicts>`_
| `View video/audio walkthrough <http://www.youtube.com/watch?v=GqEvacIiFzg>`_

Steps
=====

#. In ``models.py``, replace ``pass`` with the following as the first line
   in ``populate_todos`` (remembering to use autocomplete on ``.append``):

   .. code-block:: python

     todos.append({'id': 1, 'title': 'First'})

#. ``Shift-F10`` to re-run ``models.py`` and confirm that it prints
   that dictionary. (macOS: ``Ctrl-R``)

#. Change from a dictionary literal to dictionary constructor by
   clicking in the dictionary, typing ``Alt-Enter``, and choosing
   ``Convert dict literal to dict constructor``. It should now
   match:

   .. code-block:: python

     todos.append(dict(id=1, title='First'))

#. Confirm all is well with a ``Shift-F10`` re-run. (macOS: ``Ctrl-R``)

#. Change the last line in the main block, the ``print``, to print
   the first todo's id with a formatted string:

    .. code-block:: python

      print('Todo {todo_id}'.format(todo_id=todos[0]['id']))

#. Re-run (``Shift-F10``). It should now show ``Todo 1`` in the
   output. (macOS: ``Ctrl-R``)

#. How does Python's ``format`` string method work? Click on
   ``.format`` and choose ``View -> Quick Definition`` from
   the PyCharm menu.

#. Do the same with ``View -> Quick Definition`` and
   ``View -> External Documentation``. (The latter has a mis-fire.)

#. Press ``Ctrl-Alt-L`` to Reformat Code, if PyCharm shows any PEP8
   style warnings.

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in Todo Dicts
    :language: py

Analysis
========

In this small step we emphasize PyCharm automation:

- *Code Intentions*. Put your cursor somewhere, press ``Alt-Enter``,
  and let PyCharm suggest some things it can do for you.

- *Help Lookup*. You're not always going to remember everything about
  Python or some framework. PyCharm gives you two inline (non-distracting)
  ways and one external, full-page way to get context-sensitive information.

We also showed two things you'll do over and over:

- ``Shift-F10`` to re-run the selected Run Configuration (macOS: ``Ctrl-R``)

- ``Ctrl-Alt-L`` to clean up your code with Reformat Code

Extra Credit
============

#. How could we search for the Quick Definition action if we didn't
   know where it was in the menu? How could this search tell us
   the keyboard shortcut?

#. Does PEP8 get mad if you don't have a blank line at the end of a
   file? Will PyCharm's Reformat Code do the right thing for this?

#. Can the Code Intention (``Alt-Enter``) convert back from a dict
   constructor to a dict literal?

#. Can PyCharm link to external documentation for add-on packages
   such as SQLAlchemy?

#. If you Reformat Code, and it misfires, can you undo it?
