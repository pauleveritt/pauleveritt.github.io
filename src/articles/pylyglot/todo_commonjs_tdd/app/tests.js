require('./helper');
var describe = require('mocha').describe,
    it = require('mocha').it,
    expect = require('chai').expect,
    beforeEach = require('mocha').beforeEach,
    $ = require('jquery'),
    refreshToDos = require('./todo');

describe('To Do', function () {
    beforeEach(function () {
        $('body').html('<div>1</div>');
    });
    it('should have a refesh function')
    it('should start with empty ul', function () {
        expect($('li').length).equal(0);
    });
    //it('should increment to 6', function () {
    //    incrementer(5);
    //    expect($('div').text()).equal('6');
    //});
    //it('should start with 1', function () {
    //    expect($('div').text()).equal('1');
    //});
});