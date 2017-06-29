from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World! <a href="/todo/">Todos</a>'


@app.route('/todo/')
def list_todos():
    return 'Todo List'


if __name__ == '__main__':
    app.run(debug=True)
