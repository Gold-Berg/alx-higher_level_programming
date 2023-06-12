#include <python.h>

void print_python_list_info(PyObject *p);
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("{*} Size of the python List = %zd")
