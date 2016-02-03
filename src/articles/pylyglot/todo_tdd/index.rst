===============
TDD for ToDoMVC
===============

- npm install --save-dev mocha chai jsdom

- test.js::

    import {describe, it, beforeEach} from 'mocha';
    import {expect} from 'chai';
    import ToDos from './todo';
    import $ from 'jquery';

    describe('ToDo', () => {
        it('should import', () => {
            expect(1).eql(1);
        });
    });

- Mocha run configuration with --compilers js:babel-core/register