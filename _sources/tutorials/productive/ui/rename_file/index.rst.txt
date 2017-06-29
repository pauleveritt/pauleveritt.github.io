============
Rename Files
============

``epc.py`` is an ugly filename. Most Flask apps use something like
``app.py`` as the entry-point. Let's ask PyCharm's ``Project`` tool window
to help us on the renaming.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/ui/rename_file>`_
| `View video/audio walkthrough <http://www.youtube.com/watch?v=x310V0B8PsE>`_

Steps
=====

#. In the ``Project`` tool, right-click on ``epc.py``.

#. Choose ``Refactor -> Rename``.

#. Rename to ``app.py`` and click ``Refactor``.

#. Note the new filename.

#. In the menu, choose ``Run -> Edit Configurations``.

#. Note that the ``Script:`` field is now pointed at the new name.

#. Click ``Cancel`` to close the dialog.

#. Reload your browser to confirm the page is still loading.

#. In the ``Run`` tool window at the bottom, it is still pointing to
   the old name.

#. Click the green circle arrow to restart with the changed run
   configuration.

#. Reload in browser.

Analysis
========

The Project tool window helps us work with the code in our project. In
fact, it can do some of our work for us.

- *Rename Refactoring*. PyCharm has "refactorings" which do work for you.
  The Rename refactoring: changed the file name, renamed it in VCS, and
  changed the run configuration. As we'll see later, it can do more.

- *Actions everywhere*. The Rename refactoring is an "action" that we
  used with a right-click in the ``Project`` tool. That action is available
  via right-click in other places (e.g. the editor). But you can get to that
  action via the PyCharm menu, shortcuts, searching for actions, etc.
  We'll see that later in :doc:`../../navigation/index`.

Extra Credit
============

#. The web page still worked even though pointed at the old filename. Why?

#. If you opened the ``Terminal`` tool and used the command-line to rename
   the file, what would happen?
