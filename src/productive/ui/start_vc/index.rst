=====================
Start Version Control
=====================

PyCharm's ``Project`` tool is a very smart folder browser. We'll show
this by putting our Todo app under version control and seeing how
PyCharm can do work for us, with colors indicating VCS status. We
also show how PyCharm works with Python requirements.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/ui/start_vc>`_
| `View video/audio walkthrough <http://www.youtube.com/watch?v=fLA2rv--XYM>`_

Steps
=====

#. From the PyCharm menus, select
   ``VCS -> Import into Version Control -> Create Git Repository``.

#. In the popup window, select the project directory and click
   the ``OK`` button. We now have a ``.git`` directory in our
   project root directory.

#. In the ``Missing .gitignore file in GIT project``, click the
   ``Create .gitignore`` link button.

#. Scroll down and select ``Python``, then click the ``Generate`` button.

#. In the next popup -- ``Would you like to add unversioned files to
   the .gitignore file?`` -- click the ``Cancel`` link button.

#. Click the ``x`` on the ``.gitignore`` tab to close that file.

#. In Project Tool window, right-click on the ``epc.py`` file.

#. At the moment, it is red, meaning, not under version control.

#. In right-click context menu, choose ``Git -> Add to VCS``.

#. The color changes to green, indicating it is added but not committed.

#. In ``Project`` tool window, right-click on the root folder.

#. Choose ``New -> File``.

#. Provide ``requirements.txt`` and click ``Ok``.

#. In the next dialog, accept adding the new file to VCS.

#. In ``requirements.txt``, add a line for ``flask-sqlalchemy``. The
   file should look like this:

   .. literalinclude:: requirements.txt
    :caption: requirements.txt for Start VC section

#. Close ``requirements.txt`` by clicking the ``x`` on the tab.

#. You will now be prompted with
   ``Package requirement 'flask-sqlalchemy' is not satisfied``.

#. Click the ``Install requirement`` link.

#. Commit these changes to VCS with ``VCS -> Commit Changes``.

#. Type ``First commit`` in the ``Commit Message`` box.

#. Click the ``Commit`` button, then choose ``Commit`` from the button menu.

#. Note that the two files in the ``Project`` tool window are now a
   normal color.

#. Open PyCharm's Settings with ``File -> Settings``,  or use ``Ctrl-Alt-S``
   as a shortcut. (macOS: ``PyCharm -> Preferences`` and ``Cmd-,``.)

#. In Settings (aka Preferences), click on ``Tools -> Python Integrated Tools``.
   The first field shows which file is registered with PyCharm as this
   interpreter's requirements file.

#. Click ``Cancel`` to dismiss the preferences.

Analysis
========

We did a lot of small steps in this task, showing how the tool
windows can be put to work:

- *Visual cues*. Making a local Git repository caused the project tool
  to start giving us helpful visual information.

- *Tool context menus*. Entries in the project tool can be right-clicked
  on to get context sensitive menus.

We also used some other features of PyCharm:

- *Install packages*. Changing the requirements file prompted for missing
  packages, then did the work to install.

- *Git*. PyCharm is a great visual front-end for version control
  systems (VCS).

Extra Credit
============

#. Why doesn't PyCharm show the ``.git`` directory in the the file
   browser?

#. What other hidden directory did PyCharm make in the root directory?

#. Can PyCharm help you manage your ``.gitignore`` file?

#. What is the keyboard shortcut for committing a file?

#. How do you delete a file from the filesystem *and* from VCS?

#. Besides the project tool window, where else does the color for a
   file's VCS status appear?

#. What is the color for a file that has uncommitted changes?

#. What is the visual indicator on a project tool's file when it has
   a major Python error in it?

#. When installing a Python package via Project Interpreter preferences,
   can you simultaneously record it in the ``requirements.txt``?

