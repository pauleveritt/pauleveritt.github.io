===============
TDD for ToDoMVC
===============

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_tdd>`_

In :doc:`../jsdom/index` we saw using Mocha and Chai for frontend unit
tests, with jsdom as a fake "browser", to let jQuery work. Let's write
some tests for our ToDoMVC frontend.

Source Code
===========

#. *Install dependencies*. We need mocha, chai, and jsdom:

   .. code-block:: bash

        $ npm install --save-dev mocha chai jsdom

#. *Small first test*. Let's make a file ``tests.js`` with one test:

   .. code-block:: js

        import $ from 'jquery';
        import {describe, it, beforeEach} from 'mocha';
        import {expect} from 'chai';
        import ToDos from './todo';

        describe('ToDo', () => {
            it('should import', () => {
                expect(ToDos).to.be.a('function');
            });
        });

#. *PyCharm run configuration*. Make a ``Mocha`` run configuration,
   pointed at this ``tests`` file, with ``Extra Mocha options`` set to::

    --compilers js:babel-core/register

#. *Run it*.

#. *Add test setup*. Make a function inside ``describe`` to setup each
   test:

   .. code-block:: js

    beforeEach(() => {
        $('body').html(`
            <input id="newName"/>
            <ul id="todoList"></ul>
            `
        );

        // Avoid confusion, just reset these. Each test has to set.
        $.get = null;
        $.ajax = null;
    });

#. *Helper module*. jQuery wants some globals before import. Let's
   make a ``helper.js`` module which we import before any other
   imports:

   .. code-block:: js

        import jsdom from 'jsdom';
        global.document = jsdom.jsdom('<body></body>');
        global.window = document.defaultView;

#. *Import helper.js*.

#. *Add tests*. Add, one-by-one, each of the tests:

   .. literalinclude:: app/tests.js
        :language: js
        :caption: ToDoMVC TDD tests.js
