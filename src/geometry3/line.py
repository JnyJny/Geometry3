'''
'''

from dataclasses import dataclass
from .point import Point


@dataclass
class Line:
    '''
    A line with infinite length defined by two points; A and B.
    '''
    A: Point
    B: Point


class Ray(Line):
    pass


class Segment(Line):

    @property
    def length(self):
        return self.A.distance(self.B)
