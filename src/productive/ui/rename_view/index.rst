===========
Rename View
===========

Our view function is named ``hello_world``. Let's change it to ``home_page``.
Along the way, let's get introduced to some of the UI elements in PyCharm.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/ui/rename_view>`_

Steps
=====

#. Close all the editor tabs by clicking the ``x`` for each.

#. Click the red button in the left side of the ``Run`` window at the bottom.

#. Click the ``4. Run`` tab button in the bottom of the screen to close that
   tool window.

#. Click the ``1. Project`` tab button in the left edge of window to collapse
   the Project Tool window.

#. Click it again to re-open.

#. In the Project Tool window, click to expand the top folder.

#. In the Project Tool window toolbar, click the collapse button (|collapse|).

#. Click the ``epc`` folder to expand/open it.

#. Double-click the ``epc.py`` file to open it in the editor.

#. Click somewhere inside the symbol ``hello_world``, putting the caret in that
   function name.

#. From the PyCharm menu, choose ``Refactor -> Rename``.

#. In the dialog box, change ``hello_world`` to ``home_page`` and click
   ``Refactor``.

#. In the next prompt, click the ``Do Refactor`` button.

#. Afterwards, your ``epc.py`` file should look like this:

   .. literalinclude:: epc.py
    :caption: epc.py
    :language: py
    :emphasize-lines: 6-8

#. In the PyCharm top toolbar, click the green play button to run your
   Python app.

#. Reload your browser to confirm all is well.

.. |COLLAPSE| image:: https://www.jetbrains.com/help/img/idea/icon_collapse_all_on_title_bar.png


Analysis
========

In this task we made a small change, but used that change to explore
much of the PyCharm UI.

- *Close tabs*. The editor has tabs which can be closed (plus lots more
  that we'll see later.)

- *Placement*. The IDE has "tool windows" that are placed on the left,
  bottom, and right.

- *Toggle*. These tool windows can be toggled open and closed.

- *Mini-UI*. Inside the window, each tool has its own little UI (toolbars,
  tabs, etc.)

- *Files are good*. The Project tool is pretty important, obviously.

- *Editor tabs*. The Editor manages files in one or more tabs.

Extra Credit
============

#. What does the ``1`` in the ``1. Project`` tool window button indicate?

#. How do you move a tool window button to another part of the screen?

#. What are some ways you can close an editor tab besides clicking the
   ``x``?

#. Same for closing/opening tool windows...what other ways are there,
   instead of using the mouse?

#. How do you use the ``Structure`` tool?

#. In the Project tool, the ``templates`` directory is a purple. Why?

#. Can you have more than one tab visible at once?

