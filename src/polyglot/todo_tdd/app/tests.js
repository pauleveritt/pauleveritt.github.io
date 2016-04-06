import './helper';
import $ from 'jquery';
import {describe, it, beforeEach} from 'mocha';
import {expect} from 'chai';
import ToDos from './todo';

describe('ToDo', () => {
    let sampleData = [
        {id: 1, name: 'One'},
        {id: 2, name: 'Two'}
    ];
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

    it('should import', () => {
        expect(ToDos).to.be.a('function');
    });

    it('should start with a ul and no li', () => {
        expect($('#todoList').length).eql(1);
        expect($('#todoList li').length).eql(0);
    });

    it('should do an initial render', () => {
        $.get = () => new $.Deferred().resolve({objects: sampleData});
        new ToDos();
        expect($('#todoList li').length).eql(sampleData.length);
    });

    it('should delete an item', () => {
        $.get = () => new $.Deferred().resolve({objects: sampleData});
        let todos = new ToDos();
        expect($('#todoList li').length).eql(sampleData.length);

        // Wire up $.ajax to simulate HTTP DELETE, then $.get to return
        // only one item
        $.ajax = () => new $.Deferred().resolve();
        $.get = () => new $.Deferred().resolve({
            objects: [sampleData[0]]
        });
        todos.delete(2);
        expect($('#todoList li').length).eql(sampleData.length - 1);
    });


});