import time
import random
import copy
from realizations import *

max_numbers = (10, 100, 1000, 10**6, 10**10, 10**100, 10**1000, 10**10000, 10**20000)

for max_number in max_numbers:
    print(f'Max number: {max_number}')
    lst = [random.randint(1, max_number) for _ in range(50)]
    lst_ = copy.deepcopy(lst)
    start = time.time()
    lst1 = get_new_list_division(lst)
    print('Division', time.time() - start)

    start = time.time()
    lst2 = get_new_list_tricky(lst_)
    print('Not division', time.time() - start)

    print(lst1 == lst2)
