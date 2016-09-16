=================
List Todos Method
=================

Having our web app import the todos list directly isn't that smart.
What if there's some work involved, such as a database query? Let's
change to use a class method. We can get PyCharm to help us with
the refactoring.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/productivity/list_todos_method>`_

Steps
=====

#. In ``models.py``, let's add a method ``list`` to the class. After the
   ``__repr__`` method, start a new method by typing ``def list(``. Hit
   ``enter`` then press ``Shift-Enter`` to start a new line.

#. In the body of this method, type ``return t`` and press ``enter`` to
   accept the autocomplete of ``todos``.

#. ``list`` has a squiggly underline. Mouse-over it. PyCharm helpfully
   tells you ``Method 'list' may be 'static'``.

#. Can PyCharm do this change for us? Click on ``list`` and press
   ``Alt-Enter``. Choose ``Make method static``.

#. Press ``Ctrl-Alt-L`` to clean up any line formatting complaints.
   (macOS: ``Cmd-Alt-L``)

#. Our ``__repr__`` is doing a lot. Perhaps we can refactor it. First, let's
   extract the formatting into a property ``display`` that can be overridden
   by subclasses.

#. Click in the ``.format`` of ``__repr__`` (or anywhere on the return line)
   and choose ``Refactor -> Extract -> Method``.

#. In the popup's ``Method name:`` box, enter ``display`` and click ``OK``.

#. PyCharm makes a new ``display`` method with the logic, and changes
   ``__repr__`` to call it.

#. Let's say you changed your mind. Press ``Ctrl-Z`` to undo and all of that
   work is undone in one unit. (macOS: ``Cmd-Z``)

#. Or you decided you wanted it. Press ``Shift-Cmd-Z`` to redo. (macOS:
   ``Shift-Cmd-Z``)

#. Something looks fishy about ``display``. Click somewhere in ``def display``
   and press ``Alt-Enter``. Sure enough, PyCharm can convert it to a
   property. Select ``Convert method to property``. PyCharm adds the
   decorator and changes all usages, such as ``__repr__``.

#. Next, we'd like the format string to be parameterizable. Click once inside
   ``'Todo {todo_id}'`` then expand the selection by pressing ``Ctrl-W``
   three times. PyCharm's selection should highlight the single quotes.
   (macOS: ``Alt-Up``)

#. Open the ``Refactor`` popup with ``Ctrl-Alt-Shift-T``. Choose ``Field``.
   (macOS: ``Ctrl-T``)

#. In the inline popup, change ``Initialize in:`` from ``current method``
   to ``constructor``, then enter ``display_fmt`` into the red box and press
   enter.

#. PyCharm has added ``self.display_fmt`` to our constructor and changed
   the ``display`` property method to use it.

#. That's a lot. Let's re-run ``models.py`` with ``Shift-F10`` to make sure
   it runs ok. *Make sure the models.py run configuration is selected.*
   (macOS: ``Ctrl-R``)

#. We can now refactor ``app.py`` to use this. On the first line inside
   ``list_todos``, type ``todos = ToDo`` and press ``Alt-Enter`` to
   import the ``ToDo`` class. Then continue typing ``.list()``, resulting in
   ``todos = ToDo.list()``.

#. Hmm, we have an unused import, as we don't get ``todos`` from ``models.py``
   any longer. PyCharm can help. ``Code -> Optimize Imports`` not only removes
   unused imports, but re-organizes your import listing based on a
   configurable policy.

#. Does the web app still work? Reload the browser and visit the todo listing
   to confirm.

#. At long last, we realize our ``ToDo`` typo, and by now, it is used in
   multiple places in multiple files. PyCharm's Rename Refactoring to the
   rescue!

#. Click in an occurrence of ``ToDo``.

#. Click on ``Refactor -> Rename``, change to ``Todo``, and click
   ``Refactor``. Confirm that all cases were fixed in both files, then
   reload your browser to confirm the web app still works. Optionally,
   re-run ``models.py``.

#. Your ``app.py`` should match the following:

   .. literalinclude:: app.py
    :caption: app.py in List Todos Method
    :language: py

#. Your ``models.py`` should match the following:

   .. literalinclude:: models.py
    :caption: models.py in List Todos Method
    :language: py

Analysis
========

Another step with quite a number of small changes:

- *Refactoring static method*. The conversion to a static method is not
  only a useful warning, but doing the work for us lets us complete the
  task without much interruption.

- *Logic refactoring*. The sequence of extracting the logic to a method,
  converting it for us into a property, then extracting the format
  string to a constructor field, really showed how PyCharm refactoring
  can keep us in the development flow.

- *Use, then auto-import*. We again see the pattern of typing in a
  symbol, then letting PyCharm generate the import.

- *Optimize Imports*. Cleaning up your imports is tedious, janitorial
  work. Let PyCharm do it for you. New in PyCharm 2016.2: configure
  how the imports are laid out, to match your preferences.

- *Project-wide Rename*. Sometimes you avoid a rename, just to avoid
  all the work to find the symbol and fix it. PyCharm makes this
  refactoring a trivial task.

Extra Credit
============

#. We use ``Alt-Shift-Up`` to extend the selection. Can this extend beyond
   the current line, to an entire block?

#. In Python, what's the difference between ``@classmethod`` and
   ``@staticmethod``?
