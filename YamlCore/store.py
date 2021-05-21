# Copyright (c) 2021 Hashz Software.
import sys

sys.path.insert(1, "..")
from Types.item_not_found import ItemNotFound

class Store:
    shelf = {}

    def add(self, k, v):
        self.shelf[k] = v
    
    def get(self, k, v):
        
        if not k in self.shelf:
            ItemNotFound(k)

        return self.shelf[k]