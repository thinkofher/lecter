from .supports import Support
from numpy import array


class AlreadySigned(Exception):
    """Raise when Node is already signed."""
    pass


class NotSignedYet(Exception):
    """Raise when Node is not signed yet."""
    pass


# TODO: maybe it should be an abstract class?
class Node:
    _signed = False

    @property
    def global_matrix_pointers(self):
        """
        Returns tuple of pointers to global stifness
        matrix and other elements of FEM equation.
        """
        try:
            return (2*self._globalid, 2*self._globalid+1)
        except AttributeError:
            raise NotSignedYet('This node is not signed.')

    def _set_globalid(self, bar_id, local_id):
        """
        Sets global id for the node.
        """
        self._set_signed()
        self._globalid = bar_id + local_id

    def _set_signed(self):
        """
        Changing status of the node to signed, and
        checks if the node is already signed.
        """
        if self._signed:
            raise AlreadySigned
        else:
            self._signed = not self._signed

    def _clean(self):
        """
        Clean information from nodes.
        """
        self._signed = False
        self._globalid = None


class Node2D(Node):
    _dim = '2D'

    def __init__(self, x=0, y=0, support=Support.free()):
        self._x = x
        self._y = y
        self.support = support

    @property
    def coordinates(self):
        '''
        Returns array of x and y coordinates of node
        in global coordinate system.
        '''
        return array([self._x, self._y])
