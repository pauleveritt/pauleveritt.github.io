from typing import Dict


# Let's pass in a dictionary
def greeting(names: Dict[str, int]) -> str:
    keys = names.keys()
    return 'Hello, {}'.format(', '.join(keys))


greeting({'jane': 10, 'john': 11, 'judy': 12})
