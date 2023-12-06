#include <Python.h>

void print_python_bytes(PyObject *p);


/**
 * print_python_list - prints the basic information abt a python ls
 * @p: A PyObject list object
 */

void print_python_list(PyObject *p)
{
	int size, mem, a;
	const char *make;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *variable = (PyVarObject *)p;

	size = variable->ob_size;
	mem = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List: %d\n", size);
	printf("[*] Allocated = %d\n", mem);

	for (a = 0; a < size; a++)
	{
		make = list->ob_item[a]->tp_name;
		printf("Element %d; %s\n", a, make);
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
	unsigned char size, a;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Python Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = (9 + 1);
	else
	{
		size = ((PyVarObject *)p)->ob_size + 1;
	}

	printf("  first %d bytes: ", size);
	for (a = 0; a < size; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (size - 1))
			printf("\n");
		else
		{
			printf(" ");
		}
	}
}
