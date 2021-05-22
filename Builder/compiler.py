# Copyright (c) 2021 Hashz Software.
import os
import sys

sys.path.insert(1, "..")

import Config.include_path as include_path
import Config.libraries as libraries

def start(p_objects, p_cmdline_store):
    
    # Compile objects
    for obj in p_objects:

        # Evaluated: eg: g++ -c -Wall -o test.obj test.cpp
        command = "%s %s %s -o %s %s" % (p_cmdline_store.get("compiler"), p_cmdline_store.get("object"), include_path._get_include_path(), obj, p_objects[obj])

        if p_cmdline_store.get("verbose"):
            print(command)
        
        # Run compiler command
        os.system(command)
    
def link(p_output, p_objects, p_cmdline_store):

    # Evaluated: eg: g++ -o test.exe test.obj
    command = "%s %s -o %s %s" % (p_cmdline_store.get("compiler"), libraries._get_libs(), p_output, p_objects)

    if p_cmdline_store.get("verbose"):
        print(command)
    
    # Run compiler command
    os.system(command)