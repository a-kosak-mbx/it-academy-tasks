from operator import itemgetter
from typing import Callable, Iterable, Optional


# Требуется реализовать функцию `merge`.
# На вход функуия принимает произвольное количество сортированных последовательностей (`iterables`),
# а также параметр `key`, который позволяет извлечь ключ из элемента последовательности.
# В случае, если элемент `key` не задан, то в качестве ключа используется элемент последовательности целиком.
# В результате работы функции мы должны получить генератор, который возвращает отсортированную последовательсноть,
# состоящую из элементов переданных последовательностей. Если значения элементов нескольких последовательностей
# совпадают, то следует возвращать их в порядке следования последовательностей.
def merge(*iterables: Iterable, key: Optional[Callable] = None) -> Iterable:
    yield


data = [
    [[1, 0], [6, 0], [9, 0], [45, 0], [79, 0], [101, 0], ],
    [[1, 1], [2, 1], [4, 1], [9, 1], [60, 1], ],
    [[3, 2], [4, 2], [10, 2], ],
    [[1, 3], [79, 3], [101, 3], [105, 3], [107, 3], [809, 3], ],
]

reference = [[1, 0], [1, 1], [1, 3], [2, 1], [3, 2], [4, 1], [4, 2], [6, 0], [9, 0], [9, 1], [10, 2], [45, 0], [60, 1],
             [79, 0], [79, 3], [101, 0], [101, 3], [105, 3], [107, 3], [809, 3]]

assert list(merge(*data, key=itemgetter(0))) == reference
