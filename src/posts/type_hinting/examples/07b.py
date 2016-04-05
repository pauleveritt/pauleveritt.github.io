from typing import Union


class Greeter:
    def __init__(self, fmt: Union[str, bool]):
        if fmt:
            self.fmt = fmt
        else:
            self.fmt = 'Hi there, {}'

    def greet(self, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter(False)
print(greeting.greet('jane'))
