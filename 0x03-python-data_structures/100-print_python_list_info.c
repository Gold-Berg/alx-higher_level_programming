#include <python.h>

void print_python_list_info(PyObject *p);
{
	const char *type;
	Py_ssize_t size = PyList_Size(p);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("{*} Size of the python List = %zd\n" size);
	printf("[*] Allocated = %zd\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *element = PyList_GetTtem(p, i);

		type = Py_TYPE(element)->tp_name;

		printf("Element %zd: %s\n", i, type);
	}
}
