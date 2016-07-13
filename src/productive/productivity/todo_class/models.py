from random import randint

todos = []


class ToDo:
    def __init__(self, title):
        self.title = title
        self.id = randint(1000, 9999)

    def __repr__(self):
        return 'Todo {todo_id}'.format(todo_id=self.id)


def populate_todos():
    todos.append(ToDo('First'))


if __name__ == '__main__':
    populate_todos()
    print(todos)
