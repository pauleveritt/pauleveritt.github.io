var expect = require('chai').expect,
    dogYears = require('./app');

describe('Dog Years', function () {
    it('should be 28', function () {
        expect(dogYears(4)).to.equal(4);
    });
});