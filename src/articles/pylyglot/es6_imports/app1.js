var $ = require('jquery');

$(document).ready(function () {
    var incrementer = require('./lib1');
    var newVal = incrementer(3);
    $('h1').text('Incrementer: ' + newVal);
});