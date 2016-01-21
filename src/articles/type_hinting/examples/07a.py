class Greeter:
    def __init__(self, fmt: str = None):
        if fmt:
            self.fmt = fmt
        else:
            self.fmt = 'Hi there, {}'

    def greet(self, name: str) -> str:
        return self.fmt.format(name)


greeting = Greeter()
print(greeting.greet('jane'))
