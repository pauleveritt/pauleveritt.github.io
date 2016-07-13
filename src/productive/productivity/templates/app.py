from flask import Flask
from flask import render_template

from models import populate_todos, Todo

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html', title='Home Page')


@app.route('/todo/')
def list_todos():
    todos = Todo.list()
    div = '<div><a href="/todo/{id}">{title}</a></div>'
    items = [div.format(id=t.id, title=t.title) for t in todos]
    return '\n'.join(items)


@app.route('/todo/<int:todo_id>')
def show_todo(todo_id):
    todo = Todo.get_id(todo_id)
    fmt = '<h1>Todo {todo_id}</h1><p>{title}</p>'
    return fmt.format(todo_id=todo.id, title=todo.title)


if __name__ == '__main__':
    populate_todos()
    app.run(debug=True)
