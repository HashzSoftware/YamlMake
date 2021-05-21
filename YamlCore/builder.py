# Copyright (c) 2021 Hashz Software.
import os
import yaml

def initialize(file):

    print("Reading YAML configuration...")

    # Read the build file
    with open(file, "r") as f:
        build = yaml.full_load(f)
    
    for attr in build:
        key, value = attr, build[attr]

        # Initialization section
        if key == "init":
            if "compiler" in value:
                print("Using compiler toolset: %s" % value["compiler"])

