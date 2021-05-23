
libpath = ""

def _set_lib_path(p_path):
    
    global libpath

    if libpath != "":
        libpath += " -L%s" % p_path
    else:
        libpath += "-L%s" % p_path

def _get_lib_path():
    return libpath

libs = ""
def _add_lib(p_lib):

    global libs

    if libs != "":
        libs += " -l%s" % p_lib
    else:
        libs += "-l%s" % p_lib

def _get_libs():
    return libs