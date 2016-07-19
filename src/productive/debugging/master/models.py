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

    @staticmethod
    def get_id(todo_id):
        return [todo for todo in todos if todo.id == todo_id][0]


def populate_todos():
    todos.append(Todo('First'))
    todos.append(Todo('Second'))
    todos.append(Todo('Third'))


if __name__ == '__main__':
    populate_todos()
    first_todo = Todo.list()[0]
    first_id = first_todo.id
    print(Todo.get_id(first_id))
