
class Node:
    """
    Internal node object, order = n. Internal nodes point
    to other nodes in the tree. Can have n+1 children.
    * Order
    * List of keys
    * List of pointers to other nodes
    - add, remove, split, binary search
    """

class Leaf(Node):
    """
    Leaf node object, order = n. Leaf nodes point to records.
    Can have n+1 children. Also contain additional sibling pointer.
    * Order
    * List of keys
    * List of pointers to records
    * Sibling pointer
    """

class BPTree():
    """
    B+ Tree object, order = n. All nodes must be at least half full.
    Root must have >= 2 entries. Search starts at root -> leaf.
    * Order
    * Root
    - search, insert, delete
    """