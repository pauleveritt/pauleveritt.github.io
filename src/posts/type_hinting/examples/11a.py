from typing import Union, List, Dict

GreetingType = Union[List[str], Dict[int, List[str]]]


def greeting(names: GreetingType) -> GreetingType:
    fmt = 'Hello, {}'
    if isinstance(names, dict):
        return [(k, fmt.format(', '.join(v))) for k, v in
                names.items()]
    else:
        return fmt.format(', '.join(names))


print(greeting(['jane', 'john', 'judy']))
print(greeting(
    {10: ['jane', 'judy'],
     11: ['john'],
     12: ['judy', 'john']
     }
))
