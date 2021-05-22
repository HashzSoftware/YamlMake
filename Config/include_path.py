# Copyright (c) 2021 Hashz Software.

path = ""

def _add_include_path(p_path):

    global path

    if path != "":
        path += " -I%s" % p_path
    else:
        path += "-I%s" % p_path

def _get_include_path():
    return path