==========
Todo Dicts
==========

We don't have any todo items to show. Let's use some handy PyCharm
machinery as we implement this: more Code Intentions, Quick Documentation,
and Reformat Code.

Steps
=====

#. In ``models.py``, insert the following as the first line in
   ``populate``:

   .. code-block:: python

     todos.append({'id': 1, 'name': 'First'})

#. ``Ctrl-R`` to re-run ``models.py`` and confirm that it prints
   that dictionary.

#. Change from a dictionary literal to dictionary constructor by
   clicking in the dictionary, typing ``Alt-Enter``, and choosing
   ``Convert dict literal to dict constructor``. It should now
   look match:

   .. code-block:: python

     todos.append({'id': 1, 'name': 'First'})

#. Confirm all is well with a ``Ctrl-R`` re-run.

#.

#.

#.

#.

#.


Analysis
========

Extra Credit
============


Todo Dicts
==========

- Add a line in __main__ to join a formatted string representation
  of the list

- Explain autocomplete of .format, with quick documentation

- TODO why does .format external documentation not go to the correct thing?

- Ctrl-R to re-run

- Remind them to run Reformat Code