from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hello World!'


@appx.route('/todo')
def list_todos ():
    x = 1
    return 'Todos List'


if __name__ == '__main__':
    app.run(debug=True)
