#include <Python.h>

int cfib (int n) {
    if (n<2)
        return n;
    else
        return cfib(n-1)+cfib(n-2);
}

static PyObject* fib(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n))
        return NULL;

    return Py_BuildValue("i", cfib(n));
}

static PyObject* version(PyObject* self) {
    return Py_BuildValue("s", "version 1.0");
}

static PyMethodDef myMethods[] = {
    {"fib", fib, METH_VARARGS, "Calculates the fibonacci values"},
    {"version", version, METH_NOARGS, "returns the version" },
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef myModule = {
    PyModuleDef_HEAD_INIT,
    "myModule",
    "Fibonacci module",
    -1,
    myMethods
};

PyMODINIT_FUNC PyInit_myModule(void) {
    return PyModule_Create(&myModule);
}