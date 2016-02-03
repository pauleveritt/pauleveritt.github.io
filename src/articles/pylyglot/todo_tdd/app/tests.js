import {describe, it, beforeEach} from 'mocha';
import {expect} from 'chai';
import ToDos from './todo';
import $ from 'jquery';

describe('ToDo', () => {
    it('should import', () => {
        expect(ToDos).to.be.a('function');
    });
});