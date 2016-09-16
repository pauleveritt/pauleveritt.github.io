from flask import Flask, request
from flask import redirect

from models import populate_todos, Todo

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World! <a href="/todo/">Todos</a>'


@app.route('/todo/')
def list_todos():
    todos = Todo.list()
    div = '''<div ><a href="/todo/{id}/delete">{title}</a>
    <form method="POST" action="/todo/{id}/delete" style="display: inline">
        <input type="submit" value="x"/>
    </form>
    </div>'''
    form = '''<form method="POST" action="add">
        <input name="todo_id" placeholder="Add todo..."/>
        </form>
    '''
    items = [div.format(id=t.id, title=t.display) for t in todos]
    items.append(form)
    return '\n'.join(items)


@app.route('/todo/<int:todo_id>')
def show_todo(todo_id):
    todo = Todo.get_id(todo_id)
    fmt = '<h1>Todo {todo_id}</h1><p>{title}</p>'
    return fmt.format(todo_id=todo.id, title=todo.title)


@app.route('/todo/add', methods=['POST'])
def add_todo():
    todo_id = request.form['todo_id']
    if todo_id:
        Todo.add(todo_id)
    return redirect('/todo/')


@app.route('/todo/<int:todo_id>/delete', methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.get_id(todo_id)
    todo.delete()
    return redirect('/todo/')


if __name__ == '__main__':
    populate_todos()
    app.run(debug=True)
