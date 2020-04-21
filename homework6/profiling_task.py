import cProfile
from realizations import *
from random import randint


def profiling_func():
    get_new_list_tricky([randint(1, 10 ** 7) for _ in range(2000)])
    get_new_list_simple([randint(1, 10 ** 7) for _ in range(2000)])
    get_new_list_division([randint(1, 10 ** 7) for _ in range(2000)])


if __name__ == '__main__':
    cProfile.run('profiling_func()')
