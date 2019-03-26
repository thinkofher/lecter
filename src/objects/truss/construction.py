class _TrussOrganizer:

    def _organize(self):
        for curr_id, bar in enumerate(self.bars):
            bar._set_globalid(curr_id)


class TrussConstruction(_TrussOrganizer):

    def __init__(self, *bars):
        self.bars = bars
        self._organize()
