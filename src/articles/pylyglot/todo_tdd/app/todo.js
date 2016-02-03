import $ from 'jquery';

export default class ToDos {

    constructor () {
        this.newName = $('#newName');
        this.todoList = $('#todoList');

        // Event handlers
        this.newName.change(() => this.create(this.newName.val()));
        this.todoList.on('click', '.delete', (evt) => {
            this.delete($(evt.target).closest('li')[0].id);
        });
        this.todoList.on('click', '.edit', (evt) => {
            // Hide currently-editing and open this one for editing
            this.todoList.find('li').removeAttr('editing');
            $(evt.target).closest('li').first().attr('editing', '1');
        });
        this.todoList.on('change', 'input', (evt) => {
            // When the revealed-input changes, update using PATCH
            let todoId = $(evt.target).closest('li')[0].id,
                data = JSON.stringify({name: $(evt.target).val()});
            this.update(todoId, data);
        });


        // On startup, go fetch the list of todos and re-draw
        this.refresh();
    }

    create (newName) {
        let payload = JSON.stringify({name: newName});
        $.post('http://localhost:5000/api/todo', payload, () => {
            this.refresh();
            this.newName.val('');
        })
    }

    delete (todoId) {
        $.ajax({url: 'http://localhost:5000/api/todo/' + todoId, type: 'DELETE'})
            .done(() => this.refresh());
    }

    update (todoId, data) {
        $.ajax({url: 'http://localhost:5000/api/todo/' + todoId, type: 'PATCH', data: data})
            .done(() => this.refresh());
    }

    renderToDo (todo) {
        return `
        <li class="list-group-item" id="${ todo.id }">
            <span>${ todo.name }</span>
            <input class="form-control input-sm" title="Edit title"
                   value="${ todo.name }"/>

            <div class="btn-group pull-right" role="group">
                <button class="btn btn-xs btn-default edit">Edit</button>
                <button class="btn btn-xs btn-default delete">Delete</button>
            </div>
        </li>
        `
    }

    refresh () {
        $.get('http://localhost:5000/api/todo', (data) => {
            this.todoList
                .html(
                    data['objects']
                        .map(todo => this.renderToDo(todo))
                        .join('\n')
                );
        });
    }
};
