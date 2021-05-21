# Copyright (c) 2021 Hashz Software.
import os
import sys

sys.path.insert(1, ".")
sys.path.insert(1, "..")

from Core import shell_helpers

from Types.argument_error import ArgumentError
from Types.arg_not_found import ArgNotFound
from Types.item_not_found import ItemNotFound

from YamlCore import builder

manual_set_build = None

# Only called if there are any command line arguments
def main():

    if len(sys.argv) > 1:

        # Parse arguments
        for l_arg in range(len(sys.argv)):
            real_arg = sys.argv[l_arg]

            if real_arg == "--version":
                print("YAML Make v%s." % shell_helpers.version)

            elif real_arg == "--help":
                print(shell_helpers.cmds["help"])

            # Manually set the build file
            elif real_arg == "-F":
                
                # If no new file is supplied
                if not len(sys.argv) > l_arg + 1:
                    ArgNotFound("Expected an argument after '-F'.")
                    quit()
                
                if not os.path.exists(sys.argv[l_arg + 1]):
                    ItemNotFound(sys.argv[l_arg + 1])

                global manual_set_build
                manual_set_build = sys.argv[l_arg + 1]

                return

            # Only throw `ArgumentError` if the l_arg position has already iterated through sys.argv[0] (the executable command)
            elif l_arg > 0:
                ArgumentError(real_arg)
                quit()

        quit()

main()

# Continue with build
builder.initialize(manual_set_build) if manual_set_build\
    else builder.initialize("build.yaml")\
    if os.path.exists("build.yaml") else ItemNotFound("build.yaml")