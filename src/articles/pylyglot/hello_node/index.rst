========================================
NodeJS for Python and PyCharm Developers
========================================

If you're a Python veteran, you probably don't think too much about
the Python interpreter itself. Sure, you think about different
versions and virtual environments. But it isn't like you won't
have one.

For frontend development, though, it's quite different. You likely
think: "Ugh, I have to run my frontend code through a browser." These
days, though, JavaScript has escaped the browser via `Node.js
<https://nodejs.org/en/>`_, an environment which resembles Python
in many ways.

In particular, with Node, you have a command-line program which can
load and interpret JavaScript and print the result. Equally, with the
bundled `npm <https://www.npmjs.com>`_ as a package manager, the
world of Node provides a way to do JavaScript development,
targeting a browser, but without a browser.

In this article we'll take a quick look at how PyCharm works as an
IDE for JavaScript development.

Running JavaScript Code
=======================

Let's presume I've installed Node via their installer, Homebrew, or
one of the many other ways. If we have a ``hello_node.js`` file in
my project, we can execute it via the Node interpreter exactly the
same ways we do Python code:

.. image:: hello_node_run.gif
    :alt: Running JavaScript Code

In this example, we do a right-click on the tab and choose "Run". PyCharm
creates a "Run Configuration" and executes the code in a tool window.
Except in this case, the run configuration isn't of *Python* Run
Configuration. It is a *Node.js* Run Configuration:

.. image:: hello_node_config.gif
    :alt: Run Configuration

Configuring the Interpreter
===========================

Where did PyCharm find the Node executable and what options are there
for configuring it? In the PyCharm preferences, the ``JavaScript``
panel holds this information:

.. image:: hello_node_pref.gif
    :alt: JavaScript Preferences

Just like with PyCharm's "Python Interpreter" settings, you can
point to the executable on disk for Node. PyCharm gives a visual
way to manage Python packages, instead of running ``pip`` from the
command-line. Same with Node: this window also lets you manage
packages instead of running ``npm`` from the command line.

JavaScript Virtual Environments?
================================

In Python we are taught to develop in isolation using virtual
environments. How does that work in Node, and how does PyCharm
support it?

First, Node is designed around a two-tier global and project
``node_modules`` directory for packages. In the case where you
want full isolation, most people use `nvm
<https://github.com/creationix/nvm>`_ as a way to have multiple,
isolated versions of Node. Once this is in place, configure
your PyCharm project to point at the correct executable for the
nvm-managed Node environment.

Isn't This Like WebStorm?
=========================

This is just a brief introduction of Node.js for Python developers,
showing how it hooks up in PyCharm. We'll cover much more,
particularly in the section on *TODO package.json* files.

Many Python developers might ask: should I use WebStorm for my
frontend development and PyCharm for my backend development? While
WebStorm does provide a UI more focused on JavaScript development,
both IDEs share the same IntelliJ foundations and JavaScript
machinery. As such, you can do your frontend development while
staying in PyCharm.

To Do
=====

- Link to WebStorm, IntelliJ, etc.

- Link to package.json section