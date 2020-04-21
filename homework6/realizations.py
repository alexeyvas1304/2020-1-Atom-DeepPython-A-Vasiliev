class IncorrectLengthException(Exception):
    pass


def get_new_list_simple(lst):
    if len(lst) < 2:
        raise IncorrectLengthException()
    new_list = [None] * len(lst)
    for i in range(len(lst)):
        res = 1
        for j in range(len(lst)):
            if i != j:
                res *= lst[j]
        new_list[i] = res
    return new_list


def get_new_list_tricky(lst):
    length = len(lst)
    if length < 2:
        raise IncorrectLengthException()
    prefixes = [1] + [None] * (length - 1)
    for i in range(length - 1):
        prefixes[i + 1] = prefixes[i] * lst[i]
    suffix = 1
    for i in range(length - 1, -1, -1):
        prefixes[i] *= suffix
        suffix *= lst[i]
    return prefixes


def get_new_list_division(lst):
    length = len(lst)
    if length < 2:
        raise IncorrectLengthException()
    zero_count = lst.count(0)

    if zero_count > 1:
        return [0] * length

    elif zero_count == 1:
        mult = 1
        for el in lst:
            if el != 0:
                mult *= el
        for i in range(length):
            lst[i] = 0 if lst[i] else mult

    else:
        mult = 1
        for el in lst:
            mult *= el
        for i in range(length):
            lst[i] = mult // lst[i]

    return lst


def get_new_list_division_new_list(lst):
    length = len(lst)
    if length < 2:
        raise IncorrectLengthException()
    new_list = [None] * length
    zero_count = lst.count(0)

    if zero_count > 1:
        return [0] * length

    elif zero_count == 1:
        mult = 1
        for el in lst:
            if el != 0:
                mult *= el
        for i in range(length):
            new_list[i] = 0 if lst[i] else mult

    else:
        mult = 1
        for el in lst:
            mult *= el
        for i in range(length):
            new_list[i] = mult // lst[i]

    return new_list


if __name__ == '__main__':
    print(get_new_list_tricky([2, 3, 5, 7]))
