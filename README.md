Description
-----------

This driver is a Python wrapper of the  peak-linux-driver (in C) for Linux.


External dependencies
---------------------

- swig

  - sudo apt-get install swig

- peak-linux-driver-7.X and peak-linux-driver-8-X

  - Please visit http://peak-system.com
  - compile the library with:
    - make NET=NO_NETDEV_SUPPORT

- gcc
- python-2.7


Library compilation
-------------------

> make


Library installation
--------------------

> sudo make install

By default the module will be installed in /usr/lib


PATH settings
-------------

Add /usr/lib to the PYTHONPATH in order to find the module.

Example: export PYTHONPATH=/usr/lib:$PYTHONPATH


