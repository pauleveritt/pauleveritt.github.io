        global.document = jsdom.jsdom('<body></body>');
        global.window = document.defaultView;
        incrementer = require('./app2');
        $ = require('jquery');
