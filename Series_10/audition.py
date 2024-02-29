# https://dodona.be/nl/courses/2802/series/29676/activities/122590180
"""
>>> A = Collection([33, [27, 30], 32, 25, [20, 24], 31, 19])
>>> A.numbers()
{19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33}
>>> len(A)
14
>>> A.normal_form()
[[19, 25], [27, 33]]
>>> print(A)
[[19, 25], [27, 33]]
>>> A
Collection([[19, 25], [27, 33]])

>>> B = Collection([22, 26, 30])
>>> A - B
Collection([[19, 21], [23, 25], [27, 29], [31, 33]])
>>> B - A
Collection([26])
>>> A | B
Collection([[19, 33]])
>>> A & B
Collection([22, 30])
>>> A ^ B
Collection([[19, 21], [23, 29], [31, 33]])

>>> C = Collection([[1, 5], [7, 7]])
>>> D = Collection([[1, 5], [7, 8]])
>>> C == Collection([1, 2, 3, 4, 5, 7])
True
>>> C == D
False
>>> C != D
True
>>> C < D
True
>>> C <= D
True
>>> C > D
False
>>> C >= D
False
>>> D > C
True
>>> D >= C
True
"""


class Collection:
    def __init__(self, collection):
        assert all(isinstance(x, int) or isinstance(x, (list, tuple)) and len(x) == 2 and x[0] <= x[1]
                   for x in collection), 'invalid collection'

        self.collection = collection

    def numbers(self):
        result = set()
        for x in self.collection:
            if isinstance(x, int):
                result.add(x)
            else:
                l, u = x
                # add 2: update()
                result.update(range(l, u + 1))
        return result

    def normal_form(self):
        periods = []
        current_period = []
        for num in sorted(self.numbers()):
            if not current_period or num - current_period[-1] == 1:
                current_period.append(num)
            else:
                periods.append(current_period)
                current_period = [num]
        if current_period:
            periods.append(current_period)

        return [period[0] if len(period) == 1 else [period[0], period[-1]] for period in periods]

    def __len__(self):
        return len(self.numbers())

    def __str__(self):
        return str(self.normal_form())

    def __repr__(self):
        return f'Collection({self.normal_form()})'

    def __sub__(self, other):
        # result = []
        # for interval in self.collection:
        #     if isinstance(interval, int):
        #         if interval not in other.numbers():
        #             result.append(interval)
        #     else:
        #         for num in range(interval[0], interval[1] + 1):
        #             if num not in other.numbers():
        #                 result.append(num)
        # return Collection(result)

        return Collection(self.numbers() - other.numbers())


    def __and__(self, other):
        # result = []
        # for interval in self.collection:
        #     if isinstance(interval, int):
        #         if interval in other.numbers():
        #             result.append(interval)
        #     else:
        #         for num in range(interval[0], interval[1] + 1):
        #             if num in other.numbers():
        #                 result.append(num)
        # return Collection(result)
        return Collection(self.numbers() & other.numbers())


    def __or__(self, other):
        # result = self.collection.copy()
        #
        # for interval in other.collection:
        #     if interval not in result:
        #         result.append(interval)
        # return Collection(result)

        return Collection(self.numbers() | other.numbers())

    def __xor__(self, other):
        return Collection(self.numbers() ^ other.numbers())

    def __lt__(self, other):
        return self.numbers() < other.numbers()

    def __le__(self, other):
        return self.numbers() <= other.numbers()

    def __eq__(self, other):
        return isinstance(other, Collection) and self.numbers() == other.numbers()

    def __ge__(self, other):
        return self.numbers() >= other.numbers()
