===============================
Pythonic JavaScript for ToDoMVC
===============================

`Source code
<https://github.com/pauleveritt/pauleveritt.github.io/tree/master/src/articles/pylyglot/todo_pythonic_js>`_

With Babel in place, we can refactor our code to use ES2015 language
features: classes, array methods, arrow functions, and more, as seen
in :doc:`../pythonic_js/index`.

Steps
=====

#. Our ``app/app.js`` switches to use "arrow functions" in two places:

   .. literalinclude:: app/app.js
        :language: js
        :caption: ToDo Pythonic JS app.js
        :emphasize-lines: 4,8

#. We now have a number of ``app/todo.js`` changes which we will
   will discuss, then show the final result.

#. *Class*. In the first step, we convert to a basic class:

    - Convert to a class and put everything in the constructor

    - Change app.js to import class and new ToDo()

#. *Methods for events*. We want our event handlers to be methods,
   for create/delete etc. This is a big code re-organization. Let's
   start with ``newName`` -> ``create``:

    - var newName -> this.newName

    - create (newName) {

    - Cut-and-paste from // Create a new to do

    - let, arrow function, name: newName, this.newName

    - Demonstrate it failing

#. *Refresh method*. Our CRUD operations finish by refreshing the list.
   Let's copy ``renderToDos`` into a new method:

    - Copy-and-paste renderToDos

    - Arrow function

    - Get rid of intermediate todos = and paste directly

    - todoList.find -> this.todoList.find

    - template -> this.template

    - Add a this.todoList and this.template

    - Replace ``refreshToDos()`` with ``this.refresh()``

    - Hook up to event handler::

        // Event handlers
        this.newName.change(() => this.create(this.newName.val()));


#. *Delete*. Bind for event and call a method.

    - Event handler::

        this.todoList.on('click', '.delete', (evt) => {
            this.delete($(evt.target).closest('li')[0].id);
        });

    - Make a delete method, passed in todoId, arrow function

- *Editing*. Close any currently-editing and open this one
  for editing:

    - Cut and paste existing handler

    - this.todoList

    - arrow function (evt)

    - $(this) -> $(evt.target)

- *Edit*. Make an event listener that calls a method:

    - Cut and paste existing handler

    - this.todoList

    - Arrow function evt

    - $(this) -> $(evt.target) in *both* places

    - var -> let

    - Move $.ajax to method, leaving behind this.update(todoId, data)

        - .done(() => this.refresh());

- *ES6 template strings*. Switch to multi-line template strings:

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

- *Remove tmpl*. It's not used:

    - Remove <script> template from index.html

    - <ul id="todoList" class="list-group"></ul>

    - Remove tmpl.js

    - Remove import

    - Remove this.tmpl

    - Remove function refreshToDos

    - Call this.render instead of refreshTodos