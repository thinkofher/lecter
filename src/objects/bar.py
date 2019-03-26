from .nodes import AlreadySigned
from numpy.linalg import norm


class _BarOganizer:

    def _set_globalid(self, bar_id):
        self._globalid = bar_id
        try:
            self._starting_node._set_globalid(bar_id, 0)
        except AlreadySigned:
            pass
        try:
            self._ending_node._set_globalid(bar_id, 1)
        except AlreadySigned:
            pass


# TODO: create a angle property
class BarAngles:

    @property
    def sin_of_angle(self):
        '''
        Returns sin of angle between bar and
        global coordinate x.
        '''
        first_ycon = self._starting_node._y
        second_ycon = self._ending_node._y
        return (second_ycon-first_ycon)/self.length

    @property
    def cos_of_angle(self):
        '''
        Returns cos of angle between bar and
        global coordinate x.
        '''
        first_xcon = self._starting_node._x
        second_xcon = self._ending_node._x
        return (second_xcon-first_xcon)/self.length


class Bar(BarAngles, _BarOganizer):

    # TODO: Create sample section obcjets for further implementation
    def __init__(self, starting_node, ending_node, section, material):
        self._starting_node = starting_node
        self._ending_node = ending_node
        self.section = section
        self.material = material

    @property
    def length(self):
        '''
        Returns length of bar.
        '''
        return norm(
                (self._starting_node.coordinates -
                 self._ending_node.coordinates)
        )
