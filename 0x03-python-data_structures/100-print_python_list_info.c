#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: the PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int size, mem_allocation, a;
	PyObject *item;

	size = Py_SIZE(p);
	mem_allocation = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", mem_allocation);

	for (a = 0; a < size; a++)
	{
		printf("Element %d: ", a);
		item = PyList_GetItem(p, a);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
