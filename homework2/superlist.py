from itertools import zip_longest
from functools import wraps


def validate_second_operand(func):
    @wraps(func)
    def wrapper(*args):
        if not isinstance(args[1], SuperList):
            raise Exception('Второй операнд не суперсписок')
        return func(*args)

    return wrapper


class SuperList(list):

    def __init__(self, lst):
        if not isinstance(lst, list):
            raise Exception('Наследование не от списка')
        for element in lst:
            if not isinstance(element, int):
                raise Exception('В переданном конструктору списке не целые числа')
        super().__init__(lst)

    @validate_second_operand
    def __add__(self, other):
        return SuperList(list(map(lambda x: x[0] + x[1], zip_longest(self, other, fillvalue=0))))

    @validate_second_operand
    def __sub__(self, other):
        return SuperList(list(map(lambda x: x[0] - x[1], zip_longest(self, other, fillvalue=0))))

    @validate_second_operand
    def __le__(self, other):
        return sum(self) <= sum(other)

    @validate_second_operand
    def __lt__(self, other):
        return sum(self) < sum(other)

    @validate_second_operand
    def __ge__(self, other):
        return sum(self) >= sum(other)

    @validate_second_operand
    def __gt__(self, other):
        return sum(self) > sum(other)

    @validate_second_operand
    def __eq__(self, other):
        return sum(self) == sum(other)

    @validate_second_operand
    def __ne__(self, other):
        return sum(self) != sum(other)


# a = SuperList([1, 2, 3, 4])
# b = SuperList([1, 4, 7, 2])
# print(a - b)
# print(a)
