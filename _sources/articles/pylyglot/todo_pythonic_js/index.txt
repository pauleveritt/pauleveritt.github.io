===============================
Pythonic JavaScript for ToDoMVC
===============================

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_pythonic_js>`_

Steps
=====

- app.js

    - Arrow functions in two places

- class

    - Convert to a class and put everything in the constructor

    - Change app.js to import class and new ToDo()

- newName -> create method

    - var newName -> this.newName

    - create (newName) {

    - Cut-and-paste from // Create a new to do

    - let, arrow function, name: newName

    - Demonstrate it failing

- refresh method

    - Cut-and-paste renderToDos

    - Arrow function

    - Get rid of intermediate todos = and paste directly

    - todoList.find -> this.todoList.find

    - template -> this.template

    - Add a this.todoList and this.template

- delete

    - Event handler::

        this.todoList.on('click', '.delete', (evt) => {
            this.delete($(evt.target).closest('li')[0].id);
        });

    - Make a delete method, passed in todoId, arrow function

- editing

    - Cut and paste existing handler

    - this.todoList

    - arrow function (evt)

    - $(this) -> $(evt.target)

- change

    - Cut and paste existing handler

    - this.todoList

    - Arrow function evt

    - $(this) -> $(evt.target) in *both* places

    - var -> let

    - Move $.ajax to method, leaving behind this.update(todoId, data)

        - .done(() => this.refresh());

- Use ES6 template strings

    - Add a renderToDo(todo) method

    - return string literal

    - Copy <li> contents into it

    - Replace todos[i] with todo

    - Change 3 syntax to ${}

    - Change render()

        - this.todoList.html()

        - Inside there

        - data['objects'].map(todo => this.renderTodo(todo))

        - .join('\n')


- Get rid of template strings

    - Remove <script> template from index.html

    - <ul id="todoList" class="list-group"></ul>

    - Remove tmpl.js

    - Remove import

    - Remove this.tmpl

    - Remove function refreshToDos

    - Call this.render instead of refreshTodos