===============
TDD for ToDoMVC
===============

- npm install --save-dev mocha chai jsdom

- test.js::

    import $ from 'jquery';
    import {describe, it, beforeEach} from 'mocha';
    import {expect} from 'chai';
    import ToDos from './todo';

    describe('ToDo', () => {
        it('should import', () => {
            expect(ToDos).to.be.a('function');
        });
    });

- Mocha run configuration with --compilers js:babel-core/register

- Add beforeEach::

    beforeEach(() => {
        $('body').html(`
            <input id="newName"/>
            <ul id="todoList"</ul>
            `
        );

        // Avoid confusion, just reset these. Each test has to set.
        $.get = null;
        $.ajax = null;
    });

- Make helper.js and add import './helper';

- Add each test