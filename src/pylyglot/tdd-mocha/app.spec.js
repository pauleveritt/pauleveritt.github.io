var expect = require('chai').expect,
    dogYears = require('./app');

describe('Dog Years', function () {

    it('should be importable', function () {
        expect(dogYears).to.be.a('function');
    });

    it('should give 28 for 4', function () {
        expect(dogYears(4)).to.equal(28);
    });

    it('should fail on a string being passed', function () {
        expect(dogYears('x')).to.deep.equal(NaN);
    });

    it('should return an integer', function () {
        expect(dogYears(4)).to.be.an('number');
    });

});