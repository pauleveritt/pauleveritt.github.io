from flask import Flask
from flask import render_template

from models import populate_todos, Todo

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home_page.html', title='Home Page')


@app.route('/todo/')
def list_todos():
    todos = Todo.list()
    return render_template('list_todos.html', title='List Todos', todos=todos)


@app.route('/todo/<int:todo_id>')
def show_todo(todo_id):
    todo = Todo.get_id(todo_id)
    return render_template('show_todo.html', title='Todo ' + str(todo_id), todo=todo)


if __name__ == '__main__':
    populate_todos()
    app.run(debug=True)
