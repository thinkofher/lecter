import unittest
from math import sqrt
from ..src.objects.bar import Bar
from ..src.objects.nodes import Node2D
from ..src.objects.materials.material import ElasticMaterial
from ..src.objects.sections import CircleBar

class TestMaterials(unittest.TestCase):

    _steel_young_m = 210e9
    _steel_pos = 0.3
    steel = ElasticMaterial(
        young_m=_steel_young_m, poisson=_steel_pos)

    _aluminium_kirhf_m = 25.5
    _aluminium_pos = 0.33
    aluminium = ElasticMaterial(
        kirchff_m=_aluminium_kirhf_m, poisson=_aluminium_pos)

    _concrete_young_m = 27e9
    _concrete_kirhf_m = 11.25e9
    concrete = ElasticMaterial(
        young_m=_concrete_young_m, kirchff_m=_concrete_kirhf_m)

    def test_kirchoff_modulus(self):
        steel_kirch_modulus = self._steel_young_m/(2*(1+self._steel_pos))
        self.assertEqual(self.steel.kirchoffs_modulus, steel_kirch_modulus)

    def test_young_modulus(self):
        alum_young_modulus = 2*self._aluminium_kirhf_m*(1+self._aluminium_pos)
        self.assertEqual(self.aluminium.youngs_modulus, alum_young_modulus)

    def test_poissons_ratio(self):
        conc_pos_ratio = ((self._concrete_young_m-2*self._concrete_kirhf_m) /
                          (2*self._concrete_kirhf_m))
        self.assertEqual(self.concrete.poissons_ratio, conc_pos_ratio)


class TestLengthOfBarObjects(unittest.TestCase):

    sample_sec = CircleBar(1)
    sample_mat = ElasticMaterial(210e9, 0.3)

    def test_length_horizontal(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=5, y=0)
        test_bar = Bar(node_1, node_2, self.sample_sec, self.sample_mat)
        self.assertEqual(test_bar.length, 5)

    def test_length_vertical(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=0, y=5)
        test_bar = Bar(node_1, node_2, self.sample_sec, self.sample_mat)
        self.assertEqual(test_bar.length, 5)

    def test_length_complex(self):
        node_1 = Node2D(x=0, y=0)
        node_2 = Node2D(x=5, y=5)
        test_bar = Bar(node_1, node_2, self.sample_sec, self.sample_mat)
        self.assertEqual(test_bar.length, 5*sqrt(2))


class TestAnglesOfBarObjects(unittest.TestCase):

    sample_sec = CircleBar(1)
    sample_mat = ElasticMaterial(210e9, 0.3)
    x1, x2, y1, y2 = 3, 5, 10, 30
    node_1 = Node2D(x=x1, y=y1)
    node_2 = Node2D(x=x2, y=y2)
    test_bar = Bar(node_1, node_2, sample_sec, sample_mat)

    manual_calc_len = sqrt((x2-x1)**2 + (y2-y1)**2)

    def test_sin_angle(self):
        manual_calc_sin_angle = (self.y2-self.y1)/self.manual_calc_len

        self.assertEqual(
            self.test_bar.sin_of_angle, manual_calc_sin_angle
        )

    def test_cos_angle(self):
        manual_calc_cos_angle = (self.x2-self.x1)/self.manual_calc_len

        self.assertEqual(
            self.test_bar.cos_of_angle, manual_calc_cos_angle
        )


if __name__ == '__main__':
    unittest.main()
