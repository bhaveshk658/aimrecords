import bisect

class Node:
    """
    Internal node object, order = n. Internal nodes point
    to other nodes in the tree. Can have n children.
    * Order
    * List of keys
    * List of pointers to other nodes
    - No add function/remove function
    """
    def __init__(self, order, keys=None, children=None):
        self.order = order
        self.keys = keys or []
        self.children = children or []

    def full(self):
        """
        Returns whether a node is full or not.
        """
        return self.order == len(self.keys) + 1

class Leaf(Node):
    """
    Leaf node object, order = n. Leaf nodes point to records.
    Can have n children. Also contain additional sibling pointer.
    * Order
    * List of keys
    * List of pointers to records
    * Sibling pointer
    """
    def __init__(self, order, keys=None, children=None, next=None):
        super().__init__(order, keys, children)
        self.next = next

    def add(self, key, value):
        """
        Add a key-value pair to the node.
        """
        # Insert key at the end
        if len(self.keys) == 0 or key > self.keys[-1]:
            self.keys.append(key)
            self.children.append(value)
            
        # Insert key at the beginning
        elif key < self.keys[0]:
            self.keys.insert(0, key)
            self.children.insert(0, value)
        
        # Insert key in appropriate spot
        else:
            for i in range(len(self.keys) - 1):
                if self.keys[i] < key and self.keys[i+1] > key:
                    self.keys.insert(i + 1, key)
                    self.children.insert(i + 1, value)
                    return

class BPTree():
    """
    B+ Tree object, order = n. All nodes must be at least half full.
    Root must have >= 2 entries. Search starts at root -> leaf.
    * Order
    * Root
    - search, insert, delete
    """
    def __init__(self, order):
        return

    def insert(self, key, value):
        return

    def __getitem__(self, key):
        return ""