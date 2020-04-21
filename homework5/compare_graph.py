import numpy as np
from matrix import Matrix
import time
from random import randint
import matplotlib.pyplot as plt


def matmul(a, b):
    d = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                d[i][j] += a[i][k] * b[k][j]
    return d


final_c_time, final_np_time, final_custom_python_time = [], [], []
for i in range(2, 21):
    c_time, np_time, custom_python_time = [], [], []
    for _ in range(15):
        a = [[randint(1, 10) for _ in range(i)] for _ in range(i)]
        b = [[randint(1, 10) for _ in range(i)] for _ in range(i)]

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

        start = time.time()
        custom_python_answer = matmul(a, b)
        result_custom_python_variant = time.time() - start

        c_time.append(result_c_variant)
        np_time.append(result_np_variant)
        custom_python_time.append(result_custom_python_variant)
    final_c_time.append(sum(c_time) / 15 * 10 ** 6)
    final_np_time.append(sum(np_time) / 15 * 10 ** 6)
    final_custom_python_time.append(sum(custom_python_time) / 15 * 10 ** 6)
fig, ax = plt.subplots()
plt.plot(range(2, 21), final_c_time, label='C')
plt.plot(range(2, 21), final_np_time, label='Numpy')
plt.plot(range(2, 21), final_custom_python_time, label='Custom python')
plt.legend()
plt.title("Сравнение времени умножения матриц")
ax.set_xlabel('размер матрицы')
ax.set_ylabel('микросекунды')
plt.show()
fig.savefig('graph')
