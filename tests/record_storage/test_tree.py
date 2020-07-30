import unittest
from aimrecords.record_storage.tree import BPTree

class TreeTests(unittest.TestCase):

    def test_additions(self):
        tree = BPTree(20)

        for i in range(2000):
            tree.insert(i, str(i))

        for i in range(2000):
            self.assertEqual(str(i), tree[i])

        tree = BPTree(4)
        nums = [1, 4, 7, 10, 17, 21, 31, 25, 19, 20, 28, 42]
        for num in nums:
            tree.insert(num, str(num))