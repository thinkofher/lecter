import unittest
from math import sqrt
from ..src.objects.bar import Bar
from ..src.objects.nodes import Node2D


class TestLengthOfBarObjects(unittest.TestCase):

    def test_length_horizontal(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=5, y=0)
        test_bar = Bar(node_1, node_2)
        self.assertEqual(test_bar.length, 5)

    def test_length_vertical(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=0, y=5)
        test_bar = Bar(node_1, node_2)
        self.assertEqual(test_bar.length, 5)

    def test_length_complex(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=5, y=5)
        test_bar = Bar(node_1, node_2)
        self.assertEqual(test_bar.length, 5*sqrt(2))


class TestAnglesOfBarObjects(unittest.TestCase):

    x1, x2, y1, y2 = 3, 5, 10, 30
    node_1 = Node2D(x=x1, y=y1)
    node_2 = Node2D(x=x2, y=y2)
    test_bar = Bar(node_1, node_2)

    manual_calc_len = sqrt((x2-x1)**2 + (y2-y1)**2)

    def test_sin_angle(self):
        manual_calc_sin_angle = (self.y2-self.y1)/self.manual_calc_len

        self.assertEqual(
            self.test_bar.sin_of_angle, manual_calc_sin_angle
        )

    def test_cos_angle(self):
        manual_calc_cos_angle = (self.x2-self.x1)/self.manual_calc_len

        self.assertEqual(
            self.test_bar.cos_of_angle, manual_calc_cos_angle
        )


if __name__ == '__main__':
    unittest.main()
