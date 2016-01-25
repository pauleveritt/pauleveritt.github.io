require('./helper');
var expect = require('chai').expect,
    $ = require('jquery'),
    incrementer = require('./app2');

describe('Hello World', function () {
    beforeEach(function () {
        $('body').html('<div>1</div>');
    });
    it('should start with 1', function () {
        expect($('div').text()).equal('1');
    });
    it('should increment to 2', function () {
        incrementer(5);
        expect($('div').text()).equal('6');
    });
    it('should start with 1', function () {
        expect($('div').text()).equal('1');
    });
});