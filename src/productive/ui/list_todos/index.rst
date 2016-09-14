================
List Todos Route
================

PyCharm's editor allows, obviously, editing. But the left and right
margins, aka the gutters, have rich functionality for helping you
code. Let's see these gutters in action by adding a second route.

Steps
=====

#. Open ``app.py`` in the editor, if it isn't already opened.

#. After the first route, add a second route with two errors and one
   warning:

   .. code-block:: python

        @appx.route('/todo/')    # Error
        def list_todos() :       # Error, extra space before :
            x = 1                # Warning, unused variable
            return 'Todo List'

#. Note the traceback in the ``Run`` tool window. Flask reloaded and
   Python exited due to ``SyntaxError: invalid syntax``.

#. The editor's right gutter has two red lines (error) and one olive
   line (warnings). Mouse over each of these to see the actual issue.

#. Correct the second error, the extra space before the colon, with
   PyCharm's ``Ctrl-Alt-L`` (Reformat Code). (macOS: ``Cmd-Alt-L``).

#. Mouse over the ``x`` to see again the actual error.

#. Click on the ``x``.

#. Click on the lightbulb that pops up and choose ``Remove statement``.

#. Change ``appx`` to ``app``.

#. Not only are the 3 gutter warnings gone, but there is a green checkbox at
   top. (Mouse over it for more detail.)

#. Right-click in the left gutter, where the line numbers are shown.

#. In the popup, turn off "Show Line Numbers".

#. Repeat to turn line numbers back on.

#. To the left of ``def home_page``, click the ``-`` to collapse the block.
   Click the ``+`` to expand.

#. Add a link to the new route by changing ``def home_page`` to return
   ``'Hello World! <a href="/todo/">Todos</a>'``. ``app.py`` should now look
   like this:

   .. literalinclude:: app.py
    :caption: app.py
    :language: py

#. In the ``Run`` window, click the green play arrow button to start the
   now-corrected Flask application.

#. Reload browser and click on the ``Todos`` link.

Analysis
========

The PyCharm IDE does a lot of work for you, and reserves areas on the screen
for interacting with you on that work. The gutters are part of this.

- *Code analysis*. PyCharm flags you when it finds something important.
  Errors and warnings are treated differently, showing up both in the
  gutter and in the editor. PyCharm Settings can be used to configure
  these errors and warnings.

- *Linting*. The code analysis is driven by PyCharm's support for various
  Python linting tools, including "PEP8" style guide tools.

- *Gutters*. PyCharm puts these gutters to more use. For example, the
  left gutter is used for breakpoints (as discussed in
  :doc:`../../debugging/index`), favorites, bookmarks, etc.

Extra Credit
============

- Delete the flask import line, then have PyCharm generate the import for you
  by clicking on ``Flask(__name__)`` and hitting ``Alt-Enter``.

- What if you don't want PEP8 issues to show up as warnings?

- Can you turn off line numbers only for one tab?

- Does the collapse/expand state survive closing and re-opening a file?
  Where is that information stored?
