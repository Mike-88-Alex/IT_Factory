from Teme_sedinta_7 import FormaGeometrica, Patrat, Cerc
from abc import ABC, abstractmethod
import unittest
import pytest
from math import pi


# Ex 1

class Test1(unittest.TestCase):
    def test_cerc_raza(self):
        cerc = Cerc(5)
        self.assertEqual(cerc.raza(), 5)

    def test_cerc_aria(self):
        cerc = Cerc(5)
        self.assertEqual(cerc.aria(), pi * 5 ** 2)

    def test_patrat_aria(self):
        pat = Patrat(3)
        self.assertEqual(pat.aria(), 3 * 3)


# Ex 2

class CercTsT(unittest.TestCase):

    def aria_tst(self):
        cerc = Cerc(10)
        self.assertAlmostEqual(c.aria(), pi * 10 ** 2)


class PatratTsT(unittest.TestCase):

    def aria_tst(self):
        p = Patrat(6)
        self.assertEqual(p.aria(), 36)


# Ex 3

def cerc_raza():
    cerc1 = Cerc(3)
    assert cerc1.raza() == 3


def cerc_aria():
    cerc1 = Cerc(3)
    assert cerc1.aria() == pi * 3 ** 2


def patrat_aria():
    pat = Patrat(4)
    assert pat.aria() == 16


# Ex 4

class FormaGeometrica(ABC):
    @abstractmethod
    def arie(self):
        pass

    @abstractmethod
    def perimetru(self):
        pass


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def arie(self):
        return self.latura ** 2

    def perimetru(self):
        return self.latura * 4


class Dreptunghi(FormaGeometrica):
    def __init__(self, lungime, latime):
        self.lungime = lungime
        self.latime = latime

    def arie(self):
        return self.lungime * self.latime

    def perimetru(self):
        return 2 * (self.lungime + self.latime)


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.raza = raza

    def arie(self):
        return round(pi * self.raza ** 2, 2)

    def perimetru(self):
        return round(2 * pi * self.raza, 2)


class Test2(unittest.TestCase):
    def patrat_tst(self):
        pat = Patrat(2)
        self.assertEqual(pat.arie(), 4)
        self.assertEqual(pat.perimetru(), 8)

    def dreptunghi_tst(self):
        drept = Dreptunghi(1, 2)
        self.assertEqual(drept.arie(), 2)
        self.assertEqual(drept.perimetru(), 6)

    def cerc_tst(self):
        cerc = Cerc(3)
        self.assertEqual(cerc.arie(), pi * 3 ** 2)
        self.assertEqual(cerc.perimetru(), 2 * pi * 3)
