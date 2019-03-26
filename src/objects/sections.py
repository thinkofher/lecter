from numpy import pi, power


class Section:
    pass


class CircleBar(Section):

    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return pi*power(self._radius, 2)
