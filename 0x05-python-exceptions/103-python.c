#include <Python.h>
#include <stdio.h>


void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - Prints basic information about Python bytes
 * @p: PyObject representing a Python bytes object
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t amt = 0, a = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	amt = PyBytes_Size(p);
	printf("  size: %zd\n", amt);

	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", amt < 10 ? amt + 1 : 10);

	while (a < amt + 1 && a < 10)
	{
		printf(" %02hhx", str[a]);
		a++;
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t amt = 0;
	PyObject *obj;
	int a = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		amt = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", amt);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (a < amt)
		{
			obj = PyList_GET_ITEM(p, a);
			printf("Element %d: %s\n", a, obj->ob_type->tp_name);

			if (PyBytes_Check(obj))
			{
				print_python_bytes(obj);
			}
			else if (PyFloat_Check(obj))
			{
				print_python_float(obj);
			}
			a++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}

/**
 * print_python_float - Prints basic information about Python floats
 * @p: PyObject representing a Python float object
 */
void print_python_float(PyObject *p)
{
	double amt = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	amt = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
