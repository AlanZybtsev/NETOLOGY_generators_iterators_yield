class FlatIterator:

    def __init__(self, list_of_list, index = -1):
        self.list_of_list = list_of_list
        self.index = index

    def __iter__(self):
        self.list_sum = sum(self.list_of_list, [])
        # print(self.list_sum)
        return self

    def __next__(self):
        if self.index == len(self.list_sum) - 1:
            raise StopIteration
        self.index += 1
        return self.list_sum[self.index]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

# ______________________________________________________________________________________________________________________

import types


def flat_generator(list_of_lists):
    list_sum = sum(list_of_lists, [])
    for i in range (0, len(list_sum)):
        # print(list_sum[i])
        yield list_sum[i]


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()

# ______________________________________________________________________________________________________________________

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list(reversed(list_of_list))

    def __iter__(self):
        return self

    def __next__(self):
        while self.list_of_list:
            self.chunk = self.list_of_list.pop()
            if type(self.chunk) is not list:
                return self.chunk
            else:
                for el in reversed(self.chunk):
                    self.list_of_list.append(el)
        raise StopIteration


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

def new_list(list_of_lists_2):
    for list_ in list_of_lists_2:
        if isinstance(list_, list):
            for x in new_list(list_):
                yield x
        else:
            yield list_

if __name__ == '__main__':
    test_3()