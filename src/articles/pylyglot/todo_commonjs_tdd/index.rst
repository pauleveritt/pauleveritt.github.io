===============
TDD for ToDoMVC
===============

- ``module.exports`` in todo.js, var require in app.js

- npm install --save-dev mocha chai jsdom

- Add helper.js and test5.js as tests.js

- Get rid of IIFE and $.document ready

- todo.js

  - In the vars: $ = require('jquery')

- test.js

    - Move  template = tmpl('list_todos') into refreshToDos function

    - refreshToDos = require('./todo');