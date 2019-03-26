from numpy import array
from ..bar import Bar


class _TrussMatrixes:
    """
    Providing needed matrixes to Truss object.
    """

    @property
    def local_stifness_matrix(self):
        """
        Returns stifness matrix of trusses bar element in
        local coordinate system.
        """
        L = self.length
        A = self.section.area
        E = self.material.youngs_modulus

        return ((A*E)/L)*array([
            [1, 0, -1, 0],
            [0, 0, 0, 0],
            [-1, 0, 1, 0],
            [0, 0,  0, 0],
        ])

    @property
    def transformation_matrix(self):
        """
        Returns transformation matrix of trusses bar element.
        """
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
        """
        Returns stifness matrix of trusses bar element in
        global coordinate system.
        """
        theta = self.transformation_matrix
        k = self.local_stifness_matrix

        return theta.transpose() @ k @ theta


class TrussBar(Bar, _TrussMatrixes):
    pass
