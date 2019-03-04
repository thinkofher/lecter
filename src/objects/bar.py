from numpy import array
from numpy.linalg import norm


class Bar:

    # TODO: Create sample section obcjets for further implementation
    def __init__(self, starting_node, ending_node, section=False):
        self._starting_node = starting_node
        self._ending_node = ending_node
        self.section = section

    @property
    def length(self):
        return norm(array(
                (self._starting_node.coordinates -
                 self._ending_node.coordinates)))
