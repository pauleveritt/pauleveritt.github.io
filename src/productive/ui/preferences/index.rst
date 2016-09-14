=====================
Managing Requirements
=====================

We forgot to add Flask to our ``requirements.txt`` file. In this step we
let PyCharm do this for us, while showing the IDE's ``Settings``
window.

`Source for this step <https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/productive/ui/preferences>`_

Steps
=====

#. Open PyCharm's Settings with ``File -> Settings``,
   or use ``Ctrl-Alt-S`` as a shortcut. (On Mac,
   ``PyCharm -> Preferences`` and ``Cmd-,``.)

#. In Settings (aka Preferences), click on ``Tools -> Python Integrated Tools``.

#. Note the first field ``Package requirements file`` is pointed to our
   ``requirements.txt``.

#. While in Settings, click on ``Project -> Project Interpreter``. Note
   that ``SQLAlchemy`` is installed. It was a dependency of
   ``flask-sqlalchemy``. You can also click ``+`` to add new packages
   via PyCharm.

#. To the far right of ``Project Interpreter``, click on the gear, then choose
   ``Add Remote``. Note the options.

#. Click ``Cancel`` to dismiss the preferences.

#. In ``epc.py``, click on ``from flask import Flask``.

#. Press ``Alt-Enter`` and use the quick fix to
   `add Flask to the requirements <https://www.jetbrains.com/help/pycharm/2016.1/populating-dependencies-management-files.html>`_.

#. Open ``requirements.txt`` and see the new entry. The file should now look
   like this:

   .. literalinclude:: requirements.txt
    :caption: requirements.txt

Analysis
========

In this we looked primarily at preferences:

- *Settings dialog*. PyCharm has a visual UI for managing settings with
  lots of stuff in it. LOTS.

- *Packaging*. PyCharm can hook up to Python packaging, with two places in
  settings that make the connection.

- *Quick Fix*. We let PyCharm automate the work of putting a dependency
  into the requirements file.

Extra Credit
============

- Can the Quick Fix be used to pin the version in the ``requirements.txt``?

- Why do we specify the test runner in the Settings?

- Can you use search when moving through the Settings?

- When installing a Python package via Project Interpreter preferences,
  can you simultaneously record it in the ``requirements.txt``?

- ``flask`` is a dependency of ``flask-sqlalchemy``, per the latter's
  `setup.py dependencies <https://github.com/mitsuhiko/flask-sqlalchemy/blob/master/setup.py#L32>`_.
  Does that mean we didn't have to list it in ``requirements.txt``?
