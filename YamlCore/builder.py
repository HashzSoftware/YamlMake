# Copyright (c) 2021 Hashz Software.
import os
import sys
import yaml

sys.path.insert(1, "..")

from Types.item_not_found import ItemNotFound
from YamlCore.store import Store

import Builder.compiler as compiler

def initialize(file):

    print("Reading YAML configuration...")

    # Read the build file
    with open(file, "r") as f:
        build = yaml.full_load(f)
    
    _store = Store()
    _objects = {}

    _output = ""
    _link_objects = ""

    for attr in build:
        key, value = attr, build[attr]

        # Initialization section
        if key == "init":

            if "compiler" in value:
                print("Using compiler toolset: %s" % value["compiler"])
                _store.add("compiler", value["compiler"])

            if "object" in value:
                _store.add("object", value["object"])

            if "link" in value:
                _store.add("link", value["link"])

            if "verbose" in value:
                _store.add("verbose", value["verbose"])


        if key == "build":
            if "objects" in value:

                # Will retrieve the key name for the object (AKA: the object)
                obj = next(iter(value["objects"]))

                # LOOKING FOR IMRPOVEMENT: retrieve the source file (format: 'foo.obj: `foo.cpp`')
                src = value["objects"][list(value["objects"].keys())[0]]

                _objects[obj] = src
            
            if "link" in value:

                # Get the output name
                output = next(iter(value["link"]))
                objects = value["link"][output]

                _output = output
                _link_objects = objects

    # Begin build
    print("Starting build...")

    # Check mandatory keys
    if not "compiler" in _store.shelf:
        ItemNotFound("No set compiler was found.")
        quit()
    
    compiler.start(_objects, _store)
    compiler.link(_output, _link_objects, _store)    