from numpy import zeros


class _TrussOrganizer:

    nodes = set()

    def _organize(self):
        """
        Sets id for every node in truss.
        """
        for curr_id, bar in enumerate(self.bars):
            bar._set_globalid(curr_id)

    @property
    def nodes(self):
        nodes = set()
        for bar in self.bars:
            nodes.add(bar._starting_node)
            nodes.add(bar._ending_node)
        return nodes

    @property
    def max_id(self):
        """
        Returns max id of the nodes in the construction.
        """
        ids = ()
        for node in self.nodes:
            ids += node.global_matrix_pointers
        return max(ids)


class _TrussConStifness:

    def _init_stiff_matrix(self):
        """
        Creates a global construction stifness matrix
        filled with zeros, in global coordinates system,
        depending on the amount of nodes.
        """
        size = self.max_id + 1
        self.con_global_stifness_matrix = zeros((size, size))

    def _stifness_aggregation(self):
        """
        Aggregates global stifness matrixes of the bars.
        """
        for bar in self.bars:
            pointers = (bar._starting_node.global_matrix_pointers
                        + bar._ending_node.global_matrix_pointers)
            for id_i, j_i in enumerate(pointers):
                for id_j, j_j in enumerate(pointers):
                    self.con_global_stifness_matrix[j_i, j_j] += \
                        bar.global_stifness_matrix[id_i, id_j]


class _TrussConForces:

    def _init_forces_vector(self):
        """
        Creates a global construction forces vector
        filled with zeros, in global coordinates system,
        depending on amount of nodes.
        """
        size = self.max_id + 1
        self.con_global_forces_vector = zeros(size)

    def _forces_aggregation(self):
        """
        Aggregates global forces vector of the nodes.
        """
        for node in self.nodes:
            pointers = node.global_matrix_pointers
            forces = node.truss_forces
            for forces_id, pointer_id in enumerate(pointers):
                self.con_global_forces_vector[pointer_id] += \
                    forces[forces_id]

        # Transform vector to 2D
        self.con_global_forces_vector = \
            self.con_global_forces_vector.reshape(
                1, self.con_global_forces_vector.size)


class _TrussSolver:

    def _apply_boundaries(self):
        pass


class TrussConstruction(
        _TrussOrganizer,
        _TrussConStifness,
        _TrussConForces,
):

    def __init__(self, *bars):
        self.bars = bars
        self._organize()

    def solve(self):
        self._init_forces_vector()
        self._init_stiff_matrix()

        self._stifness_aggregation()
        self._forces_aggregation()
