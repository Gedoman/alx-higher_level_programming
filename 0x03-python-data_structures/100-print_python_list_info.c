#include <python.h>

/**
 * print_python_list_info - prints basic info about python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObjec *p)
{
	int size, alloc, i;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
        {
		printf("Element %d: ", i);

		obj = PyList_GerItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
