
from bisect import bisect_left

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

    def split(self):
        """
        Split internal node into two nodes and move self
        up as a parent.
        """
        middle = self.order // 2
        left = Node(self.order, self.keys[:middle],
                    self.children[:middle])
        right = Node(self.order, self.keys[middle:],
                        self.children[middle:])

        self.keys = [right.keys[0]]
        self.children = [left, right]

    def search(self, key):
        """
        Binary search to see where an index should be inserted.
        """
        index = bisect_left(self.keys, key)
        return index
        

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
        self.order = order
        self.keys = keys or []
        self.children = children or []
        self.next = next

    def add(self, key, value):
        """
        Add a key-value pair to the node. O(n)
        Switch to binary search (still O(n))
        """
        index = self.search(key)
        self.keys.insert(index, key)
        self.children.insert(index, value)

    def split(self):
        """
        Split internal node into two nodes and move self
        up as a parent.
        """
        middle = self.order // 2
        left = Leaf(self.order, self.keys[:middle],
                    self.children[:middle])
        right = Leaf(self.order, self.keys[middle:],
                        self.children[middle:])

        self.keys = [right.keys[0]]
        self.children = [left, right]
        left.next = right


class BPTree():
    """
    B+ Tree object, order = n. All nodes must be at least half full.
    Root must have >= 2 entries. Search starts at root -> leaf.
    * Order
    * Root
    - search, insert, delete
    """
    def __init__(self, order):
        self.root = Leaf(order)

    def insert(self, key, value):
        return

    def __getitem__(self, key):
        return ""