=====
Setup
=====

Every tutorial starts with the painful first step of getting setup. In
person, we will try to do these parts in advance, to avoid surprises and
stay on schedule.

At the end of this step, you will have a "Hello World" Flask application
running in PyCharm.

*Note: We will be in the hallway 20 minutes before the tutorial, in
front of the room, to help any installation issues. Or, come visit us
in the PyCharm booth for help.*

`View video/audio walkthrough <http://www.youtube.com/watch?v=ALlDyT-M3eA>`_

Install
=======

#. *Install Python 3.5*. You can get this from any location.

   .. note::

      For Windows, during the install, ensure you select the box to ``Add
      Python to your environment variables.``

#. *PyCharm*. Please `download PyCharm Community Edition
   <https://www.jetbrains.com/pycharm/download/>`_ and install it. For Windows,
   make sure you click the checkbox to ``Create Desktop shortcut``.

#. *Git*. We have a couple of tasks that rely on ``git`` integration. You
   can skip these tasks, but it's better if you have an installation.

#. *Browser*. Any kind of modern browser. We're not doing advanced JS.

.. note::

  For a video guide to setup, see our `Getting Started: Setup
  screencast <https://www.youtube.com/watch?v=5rSBPGGLkW0&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP&index=2>`_
  on YouTube.

Steps
=====

#. Open PyCharm Community Edition.

#. Choose ``I do not have a previous edition of PyCharm`` when asked about
   importing settings..

#. Accept the privacy policy.

#. In ``PyCharm Initial Configuration``, click ``OK`` to accept the default
   theme etc.

#. In the ``Welcome to PyCharm`` dialog, choose ``Create New Project``.

#. On the ``Interpreter line``, click on the gear at the end of the line. In
   the sub-menu, choose ``Create VirtualEnv``.

#. In the ``Create Virtual Environment`` dialog, enter ``env35`` in the
   ``Name`` field. Make sure the ``Base interpreter`` field is pointed at
   Python 3.5, then click ``OK``.

#. Back in the new project dialog, enter ``epc`` as the name of the project.

#. Click the ``Create`` button.

#. Click ``Close`` to dismiss the tips.

#. ``Tool Windows Quick Access`` in the bottom points to a button in the bottom
   left. Click that button to reveal the tool window buttons on the left, bottom,
   and right, then dismiss the popup by clicking ``Got it``.

#. Make a new Python file by choosing ``File -> New``, then choose ``File``,
   and name it ``epc.py``.

#. In the editor for ``epc.py``, enter the following for your starting Flask
   application:

   .. code-block:: python

    from flask import Flask

    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return 'Hello World!'


    if __name__ == '__main__':
        app.run(debug=True)

#. In the ``Run`` menu, choose ``Run``.

   .. note::

      You might have to wait for PyCharm's initial indexing to finish before
      the toolbar button turns green.

#. When the Run Tool window opens in the bottom, click the
   ``http://127.0.0.1:5000/`` hyperlink to open the Flask application in
   a browser.

Optional Configuration
======================

Many developers like the dark look on their themes. Let's adopt that for
this tutorial.

#. In PyCharm's menu, click ``File-Settings`` to open PyCharm preferences.

   .. note::

      This tutorial uses Windows-based keyboard shortcuts. If you are on
      Mac, we try to also provide Mac-style alternatives. For more
      help, check the ``Keymap Reference`` in PyCharm's ``Help`` menu.

#. In the preferences, go to ``Editor -> Colors & Fonts -> Fonts`` and
   for the ``Scheme:`` dropdown, choose ``Darcula``.

#. In the preferences search box, type ``theme`` and select ``Darcula``
   from the ``Theme:`` drop-down on the right.

#. Click ``OK`` to dismiss the Preferences dialog.

Analysis
========

In this setup step we did quite a number of items:

- *Python Installation*. PyCharm projects can choose from a number of
  installed Pythons, as well as make virtual environments.

- *Projects*. PyCharm projects are simple: a regular directory of your
  source files, in which PyCharm adds a ``.idea`` subdirectory for its
  project-y stuff.

- *Configuration*. PyCharm has a number of global and per-project
  settings.

Extra Credit
============

#. Can PyCharm help me see if my ``pip`` is out-of-date, and if so,
   update it?

#. Where can I compare the features in different PyCharm editions, such
   as Community, Professional, and Edu?

#. Will the Flask app restart if you make a change? Is that PyCharm
   doing the restart or PyCharm? Will it reload the browser?