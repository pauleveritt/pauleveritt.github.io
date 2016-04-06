import jsdom from 'jsdom';
global.document = jsdom.jsdom('<body></body>');
global.window = document.defaultView;
