# Copyright (c) 2021 Hashz Software.

class ArgNotFound:
    def __init__(self, arg):
        print("\033[91mArgNotFound:\033[0m %s" % arg)