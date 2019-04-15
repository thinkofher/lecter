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


class TrussNode:

    def set_truss_boundaries(self, xt, yt):
        self.set_boundaries(xt=xt, yt=yt)

    def set_truss_load(self, x_force=0, y_force=0):
        self.x_force = x_force
        self.y_force = y_force

    @property
    def truss_forces(self):
        """
        Returns array with forces in node
        specific to truss construction.
        """
        return array([self.x_force, self.y_force])

    @property
    def truss_bounadries(self):
        """
        Returns array with information abount
        boundaries in node.
        """
        return array([self.x_trans, self.y_trans])


class Node2D(Node, TrussNode):
    _dim = '2D'
    _boundaries = (False, False, False, False)

    def __init__(self, x=0, y=0, support=Support.free()):
        self._x = x
        self._y = y
        self.support = support

    def __hash__(self):
        return hash(
            (self._x, self._y)
        )

    def set_boundaries(self,
                       xt=False, xr=False,
                       yt=False, yr=False):
        """
        Determinates if node can move or rotate
        in x or y direction.
        """
        self._boundaries = (xt, xr, yt, yr)
        self._x_trans = xt
        self._y_trans = yt
        self._x_rot = xr
        self._y_rot = yr

    @property
    def boundaries(self):
        return array(self._boundaries)

    @property
    def coordinates(self):
        '''
        Returns array of x and y coordinates of node
        in global coordinate system.
        '''
        return array([self._x, self._y])
