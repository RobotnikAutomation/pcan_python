Description
-----------

This driver is a Python wrapper of the  peak-linux-driver (in C) for Linux.


External dependencies
---------------------

- swig

  - sudo apt-get install swig

- peak-linux-driver-7.X

  - Please visit http://peak-system.com

- gcc
- python-2.7


Library compilation
-------------------

> make


Library installation
--------------------

> make install

By default the module will be installed in /usr/lib


PATH settings
-------------

Add /usr/lib to the PYTHONPATH in order to find the module.

Example: export PYTHONPATH=/usr/lib:$PYTHONPATH


