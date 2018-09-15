'''
'''

from dataclasses import dataclass
from .point import Point
from .polygon import Polygon


@dataclass
class Triangle(Polygon):
    a: Point
    b: Point
    c: Point

    @property
    def vertices(self):
        return [self.a, self.b, self.c]


    @property
    def alpha(self):
        pass

    @property
    def beta(self):
        pass

    @property
    def gamma(self):
        pass

    

    @property
    def ccw(self):
        '''Result of alpha.ccw(beta, gamma) as a float.
        '''
        return self.a.ccw(self.b, self.c)

    @property
    def isCCW(self):
        '''True if alpha,beta,gama has a counter-clockwise rotation,
        else False'''
        return self.a.isCCW(self.b, self.c)

    @property
    def area(self):

        return abs(self.ccw) / 2

    @property
    def herons_area(self):
        '''
        '''
        s = self.semiperimeter
        r = s
        for v in self.vertices:
            r *= s - v
        return math.sqrt(r)

    @property
    def inradius(self):
        '''The radius of the triangle's incircle, float.
        '''

        return (self.area * 2) / self.perimeter

    @property
    def circumcenter(self):
        '''
        The intersection of the median perpendicular bisectors, Point.

        The center of the circumscribed circle, which is the circle that
        passes through all vertices of the triangle.

        https://en.wikipedia.org/wiki/Circumscribed_circle#Cartesian_coordinates_2

        BUG: only finds the circumcenter in the XY plane
        '''
        pass

        

    @property
    def is_right(self):
        return any(math.isclose(v, half_pi) for v in self.angles)

    @property
    def is_scalene(self):
        raise NotImplementedError()

    @property
    def is_equilateral(self):
        raise NotImplementedError()
