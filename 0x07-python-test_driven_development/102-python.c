#include <Python.h>

void print_python_string(PyObject *p)
{
	const char *str;

	if (PyUnicode_Check(p))
	{
		Py_ssize_t size;
		str = PyUnicode_AsUTF8AndSize(p, &size);

		printf("string object info\n");
		printf("  type: %s\n", Py_TYPE(p)->tp_name);
		printf("  length: %zd\n", size);
		printf("  value: %s\n", str);
	}

	else
	{
		fprintf(stderr, "Invalid String Object\n");
	}
}
