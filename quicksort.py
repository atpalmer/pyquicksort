

class QuickSorter(object):
    '''
    Instances hold partition state.
    Call QuickSorter.sort (classmethod) to run algorithm on a list.
    '''

    def __init__(self, items, start, stop):
        self._items = items
        self._pivot = stop - 1      # always use last list element as pivot
        self._curr = start - 1      # current element
        self._break = start - 1     # last element less than pivot

    def swap(self):
        self._break += 1
        i1 = self._break
        i2 = self._curr
        self._items[i1], self._items[i2] = self._items[i2], self._items[i1]

    def move_next(self):
        self._curr += 1
        return self._curr < self._pivot

    def partition(self):
        while self.move_next():
            if self._items[self._curr] < self._items[self._pivot]:
                self.swap()
        assert self._curr == self._pivot
        self.swap()  # swap pivot element into place
        return self._break

    @classmethod
    def sort(cls, items, start=None, stop=None):
        if start is None:
            start = 0
        if stop is None:
            stop = len(items)
        if stop - start <= 1:
            return items
        pivot = cls(items, start, stop).partition()
        cls.sort(items, start, pivot)
        cls.sort(items, pivot, stop)
        return items


def main():
    result = QuickSorter.sort([8, 6, 2, 0, 9, 4, 1, 3, 7, 5])
    print(result)
    assert result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
    main()

