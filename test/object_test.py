import unittest
from math import sqrt
from ..objects.bar import Bar
from ..objects.nodes import Node2D


class TestBarObjects(unittest.TestCase):

    def test_length_simple(self):
        node_1 = Node2D()
        node_2 = Node2D(5)
        test_bar = Bar(node_1, node_2)
        self.assertEqual(test_bar.length, 5)

    def test_length_complex(self):
        node_1 = Node2D()
        node_2 = Node2D(5, 5)
        test_bar = Bar(node_1, node_2)
        self.assertEqual(test_bar.length, 5*sqrt(2))


if __name__ == '__main__':
    unittest.main()
