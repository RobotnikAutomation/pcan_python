############################################################################
#			Copyright (c) 2014 Robotnik Automation, SLL	   #
#			    				  		   #
############################################################################
EXE			= _pcan_module.so
BUILD		     	= ./build/
LIBDIR			= ./lib/
SRC			= ./src/
PYTHONDIR		= ./pcan_python/
LIBS			= -lpcan
INC			= -I/usr/include/python2.7 -I/usr/include
INSTALLDIR		= /usr/lib


SWIG			= swig
SWIGFLAGS		= -python
CPP		        = gcc
CCFLAGS	         	= -c -fpic 
MAKE			= make
LD			= ld
LDFLAGS			= -share	

OBJECTS =	\
			$(BUILD)pcan_module.o \
			$(BUILD)pcan_module_wrap.o


default: $(LIBDIR)$(EXE)

$(BUILD)pcan_module.o : $(SRC)pcan_module.c
	$(CPP) $(CCFLAGS) $(INC) -o $(BUILD)pcan_module.o $(SRC)pcan_module.c

$(BUILD)pcan_module_wrap.o : $(SRC)pcan_module.i
	$(SWIG) $(SWIGFLAGS) $(INC) -o $(SRC)pcan_module_wrap.c -outdir $(PYTHONDIR) $(SRC)pcan_module.i 
	$(CPP) $(CCFLAGS) $(INC) -o $(BUILD)pcan_module_wrap.o $(SRC)pcan_module_wrap.c


$(LIBDIR)$(EXE) : $(OBJECTS)
	ld $(LDFLAGS) $(LIBS) $(OBJECTS) -o $(LIBDIR)$(EXE)

clean:
	rm -fv $(BUILD)*.o
	rm -fv $(LIBDIR)$(EXE)
	rm $(PYTHONDIR)pcan_module.py $(SRC)pcan_module_wrap.c

install:
	$(MAKE);
	cp $(LIBDIR)$(EXE) $(INSTALLDIR);
	python setup.py install

