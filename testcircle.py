from circles import circle_area
import unittest
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1),pi)
        self.assertAlmostEqual(circle_area(0),0)
        self.assertAlmostEqual(circle_area(2.541),pi*2.541*2.541)

    def test_value(self):
        self.assertRaises(ValueError,circle_area,-3)

    def test_type(self):
        self.assertRaises(TypeError,circle_area,2+6j)
        self.assertRaises(TypeError,circle_area,True)
        self.assertRaises(TypeError,circle_area,"Chennai")