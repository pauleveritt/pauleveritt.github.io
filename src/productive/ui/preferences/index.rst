=====================
Managing Requirements
=====================

We forgot to add Flask to our ``requirements.txt`` file. In this step we
let PyCharm do this for us, while showing the IDE's ``Preferences``
window.

Steps
=====

#. Open PyCharm's Preferences with ``PyCharm -> Preferences`` (on Mac),
   or use ``Cmd-,`` (command comma) as a shortcut.

#. Click on ``Tools -> Python Integrated Tools``.

#. Note the first field ``Package requirements file`` is pointed to our
   ``requirements.txt``.

#. While in Preferences, click on ``Project -> Project Interpreter``. Note
   that ``SQLAlchemy`` is installed. It was a dependency of
   ``flask-sqlalchemy``. You can also click ``+`` to add new packages
   via PyCharm.

#. To the far right of ``Project Interpreter``, click on the gear, then choose
   ``Add Remote``. Note the options.

#. Click ``Cancel`` to dismiss the preferences.

#. In ``epc.py``, click on ``from flask import Flask``.

#. Press ``Alt-Enter`` and use the quick fix to
   `add Flask to the requirements <https://www.jetbrains.com/help/pycharm/2016.1/populating-dependencies-management-files.html>`_.
   *TODO This is unreliable.*

#. Open ``requirements.txt`` and see the new entry. The file should now look
   like this:

   .. literalinclude:: requirements.txt


Analysis
========

In this we looked primarily at preferences:

- *Preferences dialog*. PyCharm has a visual UI for managing settings with
  lots of stuff in it. LOTS.

- *Packaging*. PyCharm can hook up to Python packaging, with two places in
  preferences that make the connection.

- *Quick Fix*. We let PyCharm automate the work of putting a dependency
  into the requirements file.

Extra Credit
============

- Can the Quick Fix be used to pin the version in the ``requirements.txt``?

- Why do we specify the test runner in the Preferences?

- Can you use search when moving through the Preferences?

- When installing a Python package via Project Interpreter preferences,
  can you simultaneously record it in the ``requirements.txt``?

- ``flask`` is a dependency of ``flask-sqlalchemy``, per the latter's
  `setup.py dependencies <https://github.com/mitsuhiko/flask-sqlalchemy/blob/master/setup.py#L32>`_.
  Does that mean we didn't have to list it in ``requirements.txt``?
