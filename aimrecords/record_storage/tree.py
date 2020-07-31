
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
    def __init__(self, order, keys=None, children=None, next=None, leaf=None):
        self.order = order
        self.keys = keys or []
        self.children = children or []
        self.next = next
        self.leaf = bool(leaf)

    def full(self):
        """
        Returns whether a node is full or not.
        """
        return self.order == len(self.keys)
    
    def is_leaf(self):
        """
        Checks if leaf node.
        """
        return self.leaf

    def search(self, key):
        """
        Binary search to see where a key should be inserted.
        Also finds index of given key.
        """
        index = bisect_left(self.keys, key)
        return index

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
        Split node into two nodes and move self
        up as a parent.
        """
        middle = self.order // 2
        left = Node(self.order, self.keys[:middle],
                    self.children[:middle], leaf=self.leaf)
        right = Node(self.order, self.keys[middle:],
                        self.children[middle:], leaf=self.leaf)

        self.leaf = False
        self.keys = [right.keys[0]]
        self.children = [left, right]
        if left.is_leaf() and right.is_leaf():
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
        self.root = Node(order, leaf=True)

    def merge_nodes(self, parent, child, index):
        """
        Merge a child node and parent node. Occurs when a node
        splits and the parent node isn't full.
        """
        parent.children.pop(index)
        pivot = child.keys[0]

        for i, item in enumerate(parent.keys):
            if pivot < item:
                parent.keys = parent.keys[:i] + [pivot] + parent.keys[i:]
                parent.children = parent.children[:i] + child.children + parent.children[i:]
                break

            elif i + 1 == len(parent.keys):
                parent.keys += [pivot]
                parent.children += child.children
                break

    def insert(self, key, value):
        """
        Insert a key-value pair into the tree.
        """
        parent = None
        child = self.root

        while not child.is_leaf():
            parent = child
            index = child.search(key)
            child = child.children[index]

        child.add(key, value)
        
        if child.full():
            child.split()

            if parent:
                while parent.full():
                    

    def __getitem__(self, key):
        node = self.root
        
        while not node.is_leaf():
            index = node.search(key)
            node = node.children[index]
        
        return node.children[node.search(key)]