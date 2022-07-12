class CyclicIterator:
    """
    циклический итератор для произвольного итерируемого объекта
    """
    def __init__(self, iterable_object):
        self.__iterable_object = iterable_object

    def __iter__(self):
        self.__iter = iter(self.__iterable_object)
        return self

    def __next__(self):
        try:
            return next(self.__iter)
        except StopIteration:
            self.__iter = iter(self.__iterable_object)
            return next(self.__iter)


if __name__ == "__main__":
    cyclic_iterator = CyclicIterator(range(3))
    for i in cyclic_iterator:
        print(i)
