class NeedMoreData(Exception):
    """Raise when, there is a lack of input data."""
    pass


class TooMuchInputData(Exception):
    """Raise when, there is too many input data."""
    pass


# TODO: Add messages to errors
# TODO: Add tests
class ElasticMaterial:

    def __init__(self, young_m=None, kirchff_m=None, poisson=None):

        # TODO: Make it more elegant
        error_ratio = 0
        for var in (young_m, kirchff_m, poisson):
            if var is not None:
                error_ratio += 1
            if error_ratio > 2:
                raise TooMuchInputData

        self._young_modulus = young_m
        self._kirchoff_modulus = kirchff_m
        self._poissons_ratio = poisson

    @property
    def youngs_modulus(self):
        if self._young_modulus is not None:
            return self._young_modulus
        else:
            try:
                return 2*self._kirchoff_modulus*(1+self._poissons_ratio)
            except TypeError:
                raise NeedMoreData

    @property
    def kirchoffs_modulus(self):
        if self._kirchoff_modulus is not None:
            return self._kirchoff_modulus
        else:
            try:
                return self._young_modulus/(2*(1+self._poissons_ratio))
            except TypeError:
                raise NeedMoreData

    @property
    def poissons_ratio(self):
        if self._poissons_ratio is not None:
            return self._poissons_ratio
        else:
            try:
                return ((self._young_modulus - 2*self._kirchoff_modulus)
                        / (2*self._kirchoff_modulus))
            except TypeError:
                raise NeedMoreData
