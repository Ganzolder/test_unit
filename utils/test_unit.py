import unittest
from utils import arrs

class TestArrs(unittest.TestCase):
    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1), 2)
        self.assertEqual(arrs.get([1, 2, 3], -2), None)

        with self.assertRaises(IndexError):
            arrs.get([], 0)

    def test_my_slice(self):
        self.assertEqual(arrs.my_slice([], 0), [])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4), [1, 2, 3])