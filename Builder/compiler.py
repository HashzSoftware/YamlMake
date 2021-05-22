# Copyright (c) 2021 Hashz Software.
import os
import sys

sys.path.insert(1, "..")

def start(p_objects, p_cmdline_store):
    
    # Compile objects
    for obj in p_objects:

        command = "%s %s -o %s %s" % (p_cmdline_store.get("compiler"), p_cmdline_store.get("object"), obj, p_objects[obj])

        if p_cmdline_store.get("verbose") == True:
            print(command)
        
        # Run compiler command
        os.system(command)
    
def link(p_output, p_objects):
    pass
        