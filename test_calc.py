from calc import sum_nums
import unittest
0
class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_nums(10,20),30)
        self.assertEqual(sum_nums(10),10)

    def test_types(self):
        self.assertRaises(TypeError,sum_nums, 10,"20")

    def test_nums(self):
        self.assertRaises(TypeError,sum_nums,"10","20")

    def test_result(self):
        self.assertNotEqual(TypeError,sum_nums,'1020')