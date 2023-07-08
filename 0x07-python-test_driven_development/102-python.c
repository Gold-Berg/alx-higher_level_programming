#include <Python.h>
#include <stdio.h>

/**
* print_python_string - Print information about a Python string object
* @p: Pointer to the Python object
*/
void print_python_string(PyObject *p)
{
Py_ssize_t length;
wchar_t *wstr;

printf("[.] string object info\n");

if (!PyUnicode_Check(p))
{
printf(" [ERROR] Invalid String Object\n");
return;
}

length = PyUnicode_GET_LENGTH(p);

wstr = PyUnicode_AsWideCharString(p, NULL);

printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object");
printf("  length: %zd\n", length);
printf("  value: %ls\n", wstr);

PyMem_Free(wstr);
}
