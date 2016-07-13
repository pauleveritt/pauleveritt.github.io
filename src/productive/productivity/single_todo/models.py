from random import randint

todos = []


class Todo:
    def __init__(self, title):
        self.title = title
        self.display_fmt = 'Todo {todo_id}'
        self.id = randint(1000, 9999)

    def __repr__(self):
        return self.display

    @property
    def display(self):
        return self.display_fmt.format(todo_id=self.id)

    @staticmethod
    def list():
        return todos


def populate_todos():
    todos.append(Todo('First'))


if __name__ == '__main__':
    populate_todos()
    print(todos)
