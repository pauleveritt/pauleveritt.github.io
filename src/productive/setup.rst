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

Install
=======

#. *Install Python 3.5*. You can get this from any location. For Windows, during
   the install, ensure you select the box to put Python on your Path.

#. *PyCharm Professional*. Please `download PyCharm Professional
   <https://www.jetbrains.com/pycharm/download/>`_, as this course uses
   Flask. You can request a 30 day evaluation, or wait for us to give out
   evaluation keys at the conference.

#. *Git*. We have a couple of tasks that rely on ``git`` integration. You
   can skip these tasks, but it's better if you have an installation.

#. *Browser*. Any kind of modern browser. We're not doing advanced JS.

.. note::

  For a video guide to setup, see our `Getting Started: Setup
  screencast <https://www.youtube.com/watch?v=5rSBPGGLkW0&list=PLQ176FUIyIUZ1mwB-uImQE-gmkwzjNLjP&index=2>`_ on
  YouTube.

Steps
=====

#. Open PyCharm Professional.

#. Say no to importing settings.

#. Supply the license key.

#. In ``PyCharm Initial Settings``, click ``OK`` to accept the defaults.

#. In the ``Welcome to PyCharm`` dialog, choose ``Create New Project``.

#. In the next panel, choose ``Flask`` from the left-hand side.

#. On the right-hand side, click the ``...`` at the right end of the
   ``Interpreter`` line and choose ``Create VirtualEnv``.

#. In the ``Create Virtual Environment`` dialog, create a virtual environment
   based on your installed Python 3.5, somewhere on your system. (For example, in
   ``~/virtualenvs/epc`` for EuroPython.)

#. Back in the new project dialog, enter ``epc`` as the name of the project.

#. Click the ``Create`` button.

#. Click ``Close`` to dismiss the tips.

#. ``Tool Windows Quick Access`` in the bottom points to a button in the bottom
   left. Click that button to reveal the tool window buttons on the left, bottom,
   and right, then dismiss the popup by clicking ``Got it``.

#. Change the last line to read ``app.run(debug=True)``.

#. In the toolbar, click the green arrow play button to run the Flask
   application.

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

      This tutorial uses Mac-based keyboard shortcuts. If you are on
      Windows or Linux, no problem. Use ``Ctrl`` instead. For more
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

- *Projects*. PyCharm projects are a directory on disk, created from
  a project template. PyCharm Professional adds support for a number
  of web-based frameworks.

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