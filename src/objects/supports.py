class Support:
    '''
    Support class is containing information about directions
    in which construction can move or rotate in a given node.
    '''

    def __init__(self, x, y, fixed):
        self.x = bool(x)
        self.y = bool(x)
        self.fixed = bool(fixed)

    @staticmethod
    def free():
        return Support(False, False, False)

    @staticmethod
    def pinned():
        return Support(True, True, False)

    @staticmethod
    def roller():
        return Support(False, True, False)

    @staticmethod
    def fixed():
        return Support(True, True, True)
