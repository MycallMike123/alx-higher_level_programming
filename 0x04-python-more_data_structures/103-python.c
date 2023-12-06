#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints the basic information abt a python ls
 * @p: A PyObject list object
 */

void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int a;
	const char *make;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);

	for (a = 0; a < size; a++)
	{
		make = list->ob_item[a]->ob_type->tp_name;
			printf("Element %i; %s\n", a, make);
		if (strcmp(make, "bytes") == 0)
		{
			print_python_bytes(list->ob_item[a]);
		}
	}
}

/**
 * print_python_bytes - prints information about python bytes
 * @p: A PyObject list object
 */

void print_python_bytes(PyObject *p)
{
	long int size;
	int a;
	char *try = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", try);

	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (a = 0; a <= size && a < 10; a++)
		printf(" %02hhx", try[a]);
	printf("\n");
}
