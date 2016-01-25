=====================
Introduction to Mocha
=====================

Python has a strong history with unit testing. In JavaScript? Not so
much, as driving a browser is a pain. But with the emergence of
NodeJS, unit testing with test runners like
`Mocha <http://mochajs.org>`_, it's now more feasible to do TDD.

This article introduces a small amount of Mocha, apart from any
particular application. Like our other Polyglot articles, it's
written from a Python perspective.

Test Runners, Assertions, Mocks
===============================

The Python standard library has long had the ``unittest`` module
as the de-facto unit testing option for test suites, fixtures,
and assertions. While recent alternatives such as ``pytest``
have gained traction, most Python developers are familiar with
the built-in test support.

JavaScript isn't anywhere close to that. Over the years different
browser-based solutions appeared, but not only did none gain
a majority, the idea of testing itself never took hold. Most
JavaScript developers have never written a test. It's just not
in the culture.

Recently that has begun to change, particularly with
outside-the-browser environments such as NodeJS. Mocha is a
popular test runner for NodeJS. People often extend Mocha to
use `Chai <http://chaijs.org>`_ for assertions and
`Sinon.JS <http://sinonjs.org>`_ for mocking.

Usually with this approach, you remove the browser and run
in NodeJS. Let's talk about that for a moment.

Browserless
===========

This is a funky idea. It's very important, though, so let's go
through it.

Developing via a browser is way, *WAY* different than Python
development. Type, save, change window, reload browser, change
back. And heaven help you if you need to debug.

Wouldn't it be great if you could code the core logic without a
browser, and only check the browser when you needed to? Even better,
wouldn't it be great if we could get into a zen-like TDD mode of
web application development?

We can, and that's what we'll look at in this step. Two key points:

- *Fake DOM*. Many frameworks, such as jQuery, expect there to be
  a DOM. Your code won't even load without it. Fortunately there
  are solutions, such as `jsdom <https://github.com/tmpvar/jsdom>`_
  which simulate what you need.

- *Written for unit testing*. Just like with Python, you can
  write your code in a way that promotes testability by isolating
  the connection to external libraries. Ideally your framework
  would support this as well, through things like Dependency
  Injection.

Installation
============

Let's start with an empty directory. As we explained in
**The Other Step**, we make a "package" in NodeJS using the
``npm init`` command. We'll pass the ``--yes`` flag to let ``npm``
answer yes to all the questions:

.. code-block:: bash

    $ npm init --yes

Remember that this directory is like a virtual environment in
Python, albeit like one that has ``with-site-packages`` set to
true. That is, NodeJS looks in your local ``node_modules`` first
and then in the global environment for a package.

Let's install Mocha and Chai *locally* and save them as development
dependencies in our ``package.json``:

.. code-block:: bash

    $ npm install --save-dev mocha chai

After doing this command, we now have a ``node_modules`` directory
with 21 packages in it, for the Mocha and Chai dependencies.

Hello Test
==========

Now that we have a test runner (Mocha) and an assertion library (Chai),
let's write and run a test. Save the following as as ``test1.js``:

.. literalinclude:: test1.js
    :language: js
    :caption: test1.js

We use a NodeJS ``require`` to import the ``expect`` function from
the ``chai`` package. In Python, this would be:

.. code-block:: python

    from chai import expect

We then have a ``Hello World`` test suite with 1 test and one assertion.
In JS testing, functions are the way of nesting scopes.

We can run this from the command line. When you install a package with
``npm``, it often puts executable wrappers in ``node_modules/.bin``,
similar to how ``setuptools`` creates console scripts in your
virtual environments ``bin``. We can run Mocha to execute this test:

.. code-block:: bash

    $ node_modules/.bin/mocha test1.js

We should get the following output:

screenshot1

That's fairly barbaric. As discussed in **NPM RUN SCRIPTS**, we can make
it easy for ourselves and others to discover and run important,
frequent commands by adding ``package.json`` entries under ``scripts``.
In fact, ``npm init --yes`` left us a placeholder:

.. code-block:: js

      "scripts": {
        "test": "echo \"Error: no test specified\" && exit 1"
      },

Let's change it to run our Mocha test:

.. code-block:: js

      "scripts": {
        "test": "mocha test1.js"
      },

Note that we didn't have to put ``node_modules/.bin`` in front of
``mocha``, as ``npm`` knows that ``npm run`` scripts probably should
have that in the path.

This is now easier:

.. code-block:: bash

    $ npm run test

In fact, ``test`` is one of the pre-defined script names that gets a
shortcut, so you can omit the `run` part:

.. code-block:: bash

    $ npm test

But hey, this is *PyCharm*. Can't we do better than a console?

Mocha Integration for PyCharm
=============================

PyCharm has run configurations with presets for a bunch of
things you might want to run. We saw in **Hello Node** that
PyCharm has run configuration templates for NodeJS. We also
know that PyCharm supports run configurations for a number
of Python test runners.

Any chance PyCharm can put a nice UI on Mocha tests? Yes
indeed:

- TODO animated gif for adding a mocha test

As long as you have Mocha in your ``node_modules``, it's quite
simple:

- TODO provide steps for adding a run configuration

Now when we run our tests, instead of text output in a console,
we get a managed GUI for test running:

- Screenshot of test run

We're not really testing anything, though. Let's write a function for
incrementing a value, then test that it works.

.. note::

    We are using NodeJS-style (aka CommonJS) module syntax.
    Other examples use ES6 (aka ES2015) modules transpiled
    via Babel. We don't want that transpiler complexity
    polluting this example. For background, read up on
    the why and how of ` JavaScript modules
    <https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc`_.

First we create our module, ``app1.js``:

.. literalinclude:: app1.js
    :language: js
    :linenos:
    :caption: app1.js

This module exports our ``incrementer`` function as its default. Python
doesn't have a similar concept of default exports. With Python, in most
cases, everything in the top-level scope can be imported.

.. literalinclude:: test2.js
    :language: js
    :caption: test2.js
    :emphasize-lines: 2,6,7

Line 2 imports the code we want to test. The two lines in the test
execute this code and test the result.

- TODO Show PyCharm screenshot

Getting a DOM
=============

Web apps aren't this simple. Let's mix jQuery into the mix and see what
happens. First we install it from npm and save it as a dependency in
our ``package.json``:

.. code-block:: bash

    $ npm install --save jquery

We can now change our application code: instead of a function that
returns an incremented value, we increment the value of a ``<div>``:

.. literalinclude:: app2.js
    :language: js
    :caption: app2.js
    :emphasize-lines: 1,4

Our application code imports ``jquery`` using NodesJS/CommonJS
module imports, then changes the ``<div>`` content to equal
the incremented value.

When we run the test now, though, armageddon ensues:

.. code-block:: bash

    Error: jQuery requires a window with a document
        at module.exports (mocha_intro/node_modules/jquery/dist/jquery.js:29:12)
        at incrementer (mocha_intro/app2.js:4:5)
        at Context.<anonymous> (mocha_intro/test3.js:6:22)

Our first thought is: go get a browser. We could use `PhantomJS <http://phantomjs.or>`_
which has good package for Mocha support. We could start over with the
`Karma test runner <http://https://karma-runner.github.io/0.13/index.html>`_. But
these are *big* solutions. Slow, lots of fiddling necessary, and not
headless.

Enter `jsdom <https://github.com/tmpvar/jsdom>`_. This package simulates a
DOM, in your browser. While jsdom isn't perfect in simulating a browser, it is
fast and, relatively speaking, lightweight.

Let's install it as a development dependency:

.. code-block:: bash

    $ npm install --save-dev

We now can write a ``test3.js`` which imports ``jsdom`` and sets some
global variables that ``jQuery`` expects. With that in place, we can import
``jQuery``:

.. literalinclude:: test3.js
    :language: js
    :caption: test3.js

This test suite has a test that ensures we are setup correctly by
reading the initial text value of the ``<div>``. The second test
executes our function and checks the updated value of the ``<div>``.

And our tests pass! All is good...except, it isn't.

Mocha Setup and Teardown
========================

Python unit testers will spot the problem quickly: we aren't testing
in isolation! The second test modifies the ``<div>``. Any subsequent
tests wouldn't be against a fresh ``<div>``. If we added a third
test as a copy of the first, we'd see that:

.. literalinclude:: test4.js
    :language: js
    :caption: test4.js
    :emphasize-lines: 14-17

This third test fails, as the ``<div>`` has the value from the second
test, not the initial value.

Like Python's ``unittest``, Mocha has concepts of ``before``,
``beforeEach``, and ``afterEach``. Let's say we want to balance speed
and isolation. We'd like to make a DOM once for all tests, but clean
up the ``<body>`` before each test. ``test5.js`` shows this:

.. literalinclude:: test5.js
    :language: js
    :caption: test5.js
    :emphasize-lines: 6-15

Our ``Hello World`` test suite initializes ``$`` and ``incrementer``
at the test-suite scope. The ``before`` function runs once,
loading our application code once a DOM is setup and initialized. Then,
before each test, the ``<body>`` is reset to ``<div>1</div>``.

Does this look like boilerplate that you'll repeat in each test? Let's
make a ``helper.js`` module that we can import at the top of all of
our tests, to provide such initialization:

.. literalinclude:: helper.js
    :language: js
    :caption: helper.js

Our tests, as shown in ``test6.js``, now look a lot nicer by importing
``helper.js`` at the top:

.. literalinclude:: test6.js
    :language: js
    :caption: test6.js
    :emphasize-lines: 1

TDD with PyCharm
================

We now have a good basis for Pythonic testing in JavaScript, without
needing a browser. How can we get into test-driven development (TDD)
mode? Let's get PyCharm to help us with automatically-executing tests
and test debugging.

First, let's get into the flow by having our test re-run on each change
to our source. In the Mocha tool window, click the button below the
green "Rerun" button, the "Toggle auto-test" button. Then click the
green "Rerun" button:

- TODO Animated GIF for re-run

With this in place, PyCharm will re-run tests when your source or test
code changes:

- TODO Animated GIF showing a change that breaks, then fixes,
  test6.js

As a note, PyCharm doesn't require that you actually save the file
before it detects the change.

PyCharm has many options for controlling the JavaScript testing
experience. For example, we can change the delay used between
a pause in typing and re-running the tests:

- TODO Animated GIF showing changing the delay

Here's a great way to be productive: split the screen, with your
application code on the left and your tests on the right:

- TODO GIF split screen

Just like for its Python testing, PyCharm has a stupendous number of
options organizing the display of the test window:

- Hide/show passing tests

- Sort alphabetically on test name

- Show (and sort based on) duration of test run

- Automatically open at the line of an error

PyCharm also makes debugging easy during TDD. You can set a breakpoint
in your JavaScript code or your tests, step through your code, and set
watches:

- TODO Animated gif debugging breakpoint

JavaScript TDD and PyCharm Are For Real
=======================================

This only scratches the surface of what PyCharm can add for
test-driven development and JavaScript. There's much more: for
example, you can install code coverage packages and PyCharm will give
you a button and a visual display of the coverage information.

If you are a TDD-oriented Python developer, you likely
know how `PyCharm can boost Python testing productivity
<https://medium.freecodecamp.com/javascript-modules-a-beginner-s-guide-783f7d7a5fcc>`_.
With JavaScript, you might not even have considered TDD.
Once you think headless with NodeJS and Mocha, though, you can let
PyCharm orchestrate your JavaScript testing.

TODO
====

- Links to previous articles for: npm scripts, etc.

- Get package.json and npm init written up then link from here

- Intersphinx link to unittest module

- Make screenshots

- Do an "intro" for the hello_node

- Make things more Pythonic and PyCharmic

- Links to PyCharm docs

.. toctree::
    :maxdepth: 1
    :hidden:
