from typing import List


def greeting(names: List[str]) -> str:
    return 'Hello, {}'.format(', '.join(names))


greeting(['jane', 'john', 'judy'])
