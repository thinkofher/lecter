import unittest
from math import sqrt
from ..objects.bar import Bar
from ..objects.nodes import Node2D


class TestBarObjects(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
