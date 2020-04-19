import numpy as np
from matrix import Matrix
import time
from random import randint

a = [[randint(1, 10) for _ in range(5)] for _ in range(5)]
b = [[randint(1, 10) for _ in range(5)] for _ in range(5)]

a_c_variant = Matrix(a)
b_c_variant = Matrix(b)


a_np_variant = np.array(a)
b_np_variant = np.array(b)

start = time.time()
c_answer = a_c_variant.mult_matrix(b_c_variant)
result_c_variant = time.time() - start

start = time.time()
np_answer = a_np_variant @ b_np_variant
result_np_variant = time.time() - start

print("Рузультаты одинаковые" if c_answer==np_answer.tolist() else "Результаты разные")
print(f'C_variant:{result_c_variant}\nNumpy variant:{result_np_variant}')
print(f'C реализация быстрее в {(result_np_variant / result_c_variant):.3f} раз')
