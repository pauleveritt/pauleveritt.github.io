from flask import Flask
app = Flask(__name__)

from models import todos, populate_todos


@app.route('/')
def home_page():
    return 'Hello World! <a href="/todo/">Todos</a>'


@app.route('/todo/')
def list_todos():
    div = '<div><a href="/todo/{id}">{title}</a></div>'
    items = [div.format(id=t.id, title=t.title) for t in todos]
    return '\n'.join(items)


@app.route('/todo/<todo_id>')
def show_todo(todo_id):
    return 'Todo {todo_id}'.format(todo_id=todo_id)


if __name__ == '__main__':
    populate_todos()
    app.run(debug=True)
