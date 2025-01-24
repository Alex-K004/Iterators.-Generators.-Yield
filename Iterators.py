class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):

        self.cursor = -1
        return self

    def __next__(self, item):
        self.item = item
        self.item += self.list_of_list[self.cursor]
        self.cursor += 1
        if self.cursor == len(self.list_of_list):
            raise StopIteration
        return item

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

# Ошибка при запуске кода
#"C:\Users\Алексей\PycharmProjects\Iterators. Generators. Yield\.venv\Scripts\python.exe" "C:\Users\Алексей\PycharmProjects\Iterators. Generators. Yield\Iterators.py"
#Traceback (most recent call last):
# File "C:\Users\Алексей\PycharmProjects\Iterators. Generators. Yield\Iterators.py", line 38, in <module>
 #   test_1()
  #File "C:\Users\Алексей\PycharmProjects\Iterators. Generators. Yield\Iterators.py", line 27, in test_1
   # for flat_iterator_item, check_item in zip(
    #                                      ^^^^
#TypeError: FlatIterator.__next__() missing 1 required positional argument: 'item'
#
#Process finished with exit code 1