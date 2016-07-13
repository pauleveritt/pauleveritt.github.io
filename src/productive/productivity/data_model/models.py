todos = []


def populate_todos():
    todos.append(dict(id=1, name='First'))


if __name__ == '__main__':
    populate_todos()
    print('Todo {todo_id}'.format(todo_id=todos[0]['id']))
