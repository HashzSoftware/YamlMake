# Copyright (c) 2021 Hashz Software.

class ArgumentError:
    def __init__(self, err):
        print("\033[91mArgumentError:\033[0m %s" % err)