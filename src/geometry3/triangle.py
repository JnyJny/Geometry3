'''
'''

from dataclasses import dataclass
from .point import Point
from .polygon import Polygon

@dataclass
class Triangle(Polygon):
    A : Point
    B : Point
    C : Point

    @property
    def vertices(self):
        return [self.A, self.B, self.C]

    @property
    def is_right(self):
        raise NotImplementedError()

    @property
    def is_scalene(self):
        raise NotImplementedError()

