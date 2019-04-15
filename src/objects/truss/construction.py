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


class _TrussConstructionMatrixes:

    def _init_global_matrix(self):
        """
        Creates a global stifness matrix filled with zeros,
        in global coordinate system, depending on the
        amount of nodes.
        """
        self.con_global_stifness_matrix = zeros((self.max_id+1, self.max_id+1))

    def _aggregation(self):
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


class TrussConstruction(
        _TrussOrganizer,
        _TrussConstructionMatrixes
):

    def __init__(self, *bars):
        self.bars = bars
        self._organize()
