from random import randint

todos = []


class Todo:
    def __init__(self, title):
        self.display_fmt = 'Todo {todo_id}'
        self.title = title
        self.id = randint(1000, 9999)

    def __str__(self):
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
    print(todos[0])
