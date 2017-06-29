from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World! <a href="/todo/">Todos</a>'


@app.route('/todo/')
def list_todos():
    return 'Todo List <a href="/todo/1">First Todo</a>'


@app.route('/todo/<todo_id>')
def show_todo(todo_id):
    return 'Todo {todo_id}'.format(todo_id=todo_id)

if __name__ == '__main__':
    app.run(debug=True)
