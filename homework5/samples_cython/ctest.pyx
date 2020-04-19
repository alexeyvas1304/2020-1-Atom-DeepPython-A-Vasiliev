cpdef long test(int x):
    cdef long y = 1
    cdef long i
    for i in range(1, x+1):
        y *= i
    return y