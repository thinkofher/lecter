from numpy import array
from ..bar import Bar


class _TrussMatrixes:
    """
    Providing needed matrixes to Truss object.
    """

    @property
    def local_stifness_matrix(self):
        L = self.length
        A = self.section.area
        E = self.material.youngs_modulus

        return (A*E*(1/L))*array([
            [1, 0, -1, 0],
            [0, 0, 0, 0],
            [-1, 0, 1, 0],
            [0, 0,  0, 0],
        ])

    @property
    def transformation_matrix(self):
        s = self.sin_of_angle
        c = self.cos_of_angle

        return array([
            [c, s, 0, 0],
            [-s, c, 0, 0],
            [0, 0, c, s],
            [0, 0, -s, c],
        ])

    @property
    def global_stifness_matrix(self):
        pass


class TrussBar(Bar, _TrussMatrixes):
    pass
