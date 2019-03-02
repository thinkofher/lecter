from .supports import Free
from numpy import array


# TODO: maybe it should be an abstract class?
class Node:
    def _set_localid(self, id):
        self._localid = id

    def _set_globalid(self, bar_id):
        self._globalid = bar_id + self._localid


class Node2D(Node):
    _dim = '2D'

    def __init__(self, x=0, y=0, support=Free):
        self._x = x
        self._y = y
        self.support = support

    @property
    def coordinates(self):
        return array([self._x, self._y])
