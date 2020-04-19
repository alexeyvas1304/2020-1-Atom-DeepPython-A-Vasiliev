#include <Python.h>

typedef struct {
    PyObject_HEAD
} FooObject;

/* claass Foo(object): pass */

static PyTypeObject FooType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "foo.Foo",
    .tp_doc = "Foo objects",
    .tp_basicsize = sizeof(FooObject),
    .tp_itemsize = 0,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_new = PyType_GenericNew
};

static PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "foo",
    .m_doc = "module foo",
    .m_size = -1
};

PyMODINIT_FUNC
PyInit_foo(void)
{
    PyObject *m = NULL;
    if (PyType_Ready(&FooType) < 0)
        return NULL;
    if ((m = PyModule_Create(&module)) == NULL)
        return NULL;
    Py_XINCREF(&FooType);
    PyModule_AddObject(m, "Foo", (PyObject *) &FooType);
    return m;
}