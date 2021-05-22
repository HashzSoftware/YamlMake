
libpath = ""
def _set_lib_path(p_path):
    libpath = p_path

def _get_lib_path():
    return libpath

libs = ""
def _add_lib(p_lib):

    global libs

    if libs != "":
        libs += " -l%s%s" % (libpath, p_lib)
    else:
        libs += "-l%s%s" % (libpath, p_lib)

def _get_libs():
    return libs