==========
Data Model
==========

In our :doc:`previous step <../../running/list_of_todos/index>` we made
a list of todos, in a very simple manner. Let's turn that into the
start of a proper "models" file. As we do so, we'll see some PyCharm
productivity in action -- Live Templates and Quick Fixes.

Steps
=====

#. Create the new file with ``Cmd-N -> PF -> models``. The ``PF`` is a
   way PyCharm lets you narrow a list with camel case for the first
   letters in the words in a list.

#. Answer "Yes" to put under version control. PyCharm automatically adds
   ``.py`` to the given filename.

#. Enter ``todos = []`` on the first line.

#. Use Live Templates to add a main run block with ``Cmd-J main`` then
   enter.

#. When the cursor is under the ``if``, type in ``populate_todos()``.

#. Back-arrow twice to move before the parentheses.

#. ``Alt-Enter`` to open the code intentions and choose ``Create function
   'populate_todos'``.

#. With the Live Template prompt on ``pass`` in the new function, type
   ``print(todos)``. Use autocompletion to finish ``todos``.

#. Run ``models.py`` by right-clicking in the editor and choosing
   ``Run 'models'``. You should now have 2 tabs in the Run Tool window.

#. Find the other Live Templates and Code Intentions in Preferences:

    - ``Cmd-,`` to open Preferences

    - Start typing ``live`` to filter preferences by the string ``live``

    - Expand ``Python`` and click on some of the other Live Templates

    - Clear the ``live`` filter and enter ``intentions``

    - To the left of the search box, click the icon to collapse all

    - Expand the ``Python`` section

Analysis
========

Now that we have two files, we can do more with PyCharm. We saw:

- *New File*. Letting PyCharm do the work for us when creating a new
  file, including registering with VCS.

- *Live Templates*. PyCharm can automate some of the repetitive work,
  and you can even write your own.

- *Quick Fixes*. Rather than stop what you are doing, create your
  function, then come back...go ahead and type it in a usage and
  let PyCharm make the function. Use it, then define it.

Extra Credit
============

#. What directory does ``New File`` put the new file?

#. Does the camel case trick work with more than just the first letter?

#. How to do the placeholders work in Live Templates?

#. Can you share Live Templates?

