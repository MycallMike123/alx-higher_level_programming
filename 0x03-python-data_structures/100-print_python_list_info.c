#include <Python.h>

/**
 * print_python_list_info - Prints basic info about a Python list
 * @p: Pointer to a PyObject
 */

void print_python_list_info(PyObject *p)
{
	PyObject *objects;
	Py_ssize_t size, a;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (a = 0; a < size; ++a)
	{
		object = PyList_GetItem(p, a);
		printf("Element %zd: %s\n", a, Py_TYPE(object)->tp_name);
