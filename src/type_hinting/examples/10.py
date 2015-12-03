from typing import Dict


class BaseGreeter:
    fmt = 'Hi there, {}'

    def greet(self, name: str) -> str:
        return self.fmt.format(name)


class Greeter(BaseGreeter):
    def greet(self, name: str) -> Dict[str, str]:
        return dict(value=self.fmt.format(name))


greeting = Greeter()
greeting.fmt = 'Hello {}'
print(greeting.greet('jane'))
