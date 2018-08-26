import unittest
import solution


class HashCollectionTests(unittest.TestCase):
    def test_hash_collection(self):
        hash_set = solution.CustomDict(5)
        hash_set.add_val("world")
        hash_set.add_val("HellO")

        self.assertEqual("HellO world", hash_set.check_list(4))
        self.assertEqual("no", hash_set.find_val("World"))
        self.assertEqual("yes", hash_set.find_val("world"))

        hash_set.del_val("world")

        self.assertEqual("HellO", hash_set.check_list(4))
        hash_set.del_val("HellO")

        hash_set.add_val("luck")
        hash_set.add_val("GooD")

        self.assertEqual("GooD luck", hash_set.check_list(2))
