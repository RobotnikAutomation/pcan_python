/* pcan_module.i */
 %module pcan_module
 
 %include "carrays.i"
 %array_class(int, intArray);


 %{
 /* Put header files here or function declarations like below */
 #include "libpcan.h"
 #include "pcan.h"
 extern HANDLE h;
 extern char driver_info[64];
 extern int open_can(char *dev);
 extern int close_can();
 extern int get_version_info();
 extern int configure_can();
 extern int * read_can_msg();
 int send_can_msg(const int num_elements, int *data);
 %}
 
 %typemap(out) int * read_can_msg {
  int i;
  //$1, $1_dim0, $1_dim1
  $result = PyList_New(10);
  for (i = 0; i < 10; i++) {
    PyObject *o = PyInt_FromLong($1[i]);
    PyList_SetItem($result,i, o);
  }
 }

  %typemap(in) (const int num_elements, int *data) {
  int i;
  if (!PyList_Check($input)) {
    PyErr_SetString(PyExc_ValueError, "Expecting a list");
    return NULL;
  }
  $1 = PyList_Size($input);
  $2 = (int *) malloc(($1)*sizeof(int));
  for (i = 0; i < $1; i++) {
    PyObject *s = PyList_GetItem($input,i);
    if (!PyInt_Check(s)) {
        free($2);
        PyErr_SetString(PyExc_ValueError, "List items must be integers");
        return NULL;
    }
    $2[i] = PyInt_AsLong(s);
  }
 }

 %typemap(freearg) (const int num_elements, int *data) {
   if ($2) free($2);
 }
 
 %include "libpcan.h"
 %include "pcan.h"
 extern HANDLE h;
 extern char driver_info[64];
 extern int open_can(char *dev);
 extern int close_can();
 extern int get_version_info();
 extern int configure_can();
 extern int * read_can_msg();
 int send_can_msg(const int num_elements, int *data);

