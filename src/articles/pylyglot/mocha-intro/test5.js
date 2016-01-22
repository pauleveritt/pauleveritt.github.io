var expect = require('chai').expect,
    jsdom = require('jsdom');


describe('Hello World', function () {
    var $, incrementer;
    before(function () {
        global.document = jsdom.jsdom('<body></body>');
        global.window = document.defaultView;
        $ = require('jquery');
        incrementer = require('./app2');
    });
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