# Copyright (c) 2021 Hashz Software.
import os
import yaml

def initialize(file):

    print("Reading build file...")

    # Read the build file
    with open(file, "r") as f:
        build = yaml.full_load(f)
    
    for attr in build:
        key, value = attr, build[attr]
