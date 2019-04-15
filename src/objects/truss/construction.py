from numpy import zeros


class _TrussOrganizer:

    nodes = set()

    def _organize(self):
        """
        Sets id for every node in truss.
        """
        for curr_id, bar in enumerate(self.bars):
            bar._set_globalid(curr_id)
        self._set_nodes()

    # TODO: why theres 6 nodes _TrussOrganizer.nodes
    # if i define only 3 nodes
    def _set_nodes(self):
        """
        Adds nodes to the nodes tuple property of truss.
        """
        for bar in self.bars:
            self.nodes.add(bar._starting_node)
            self.nodes.add(bar._ending_node)

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
        pass


class TrussConstruction(
        _TrussOrganizer,
        _TrussConStifness,
        _TrussConForces,
):

    def __init__(self, *bars):
        self.bars = bars
        self._organize()
