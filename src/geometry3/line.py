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

    @property
    def points(self):
        return [self.A, self.B]

    @property
    def is_vertical(self):
        return self.A.x == self.B.x

    @property
    def is_horizontal(self):
        return self.A.y == self.B.y

    @property
    def is_same_z(self):
        # XXX what is this property really called?
        return self.A.z == self.B.z

    @property
    def m(self):
        '''slope parameter, Point(B-A)
        '''
        return self.B - self.A

    @property
    def length(self):
        raise ValueError('lines have infinite length')

    @property
    def normal(self):
        '''Returns a Line normal (perpendicular) to the given Line.
        '''
        d = self.m
        return Line(Point(-d.y, d.x), Point(d.y, -d.x))

    def __contain__(self, point):
        
        return self.A.is_colinear(point, self.B)


    def point_at(self, t):

        return self.A + (t * self.m)

    def t(self, point):

        if point not in self:
            raise ValueError(f'{point} is not colinear with {self}')

        return (point - self.A) / self.m


    def flip(self):
        
        self.A, self.B = self.B, self.A

    def intersects(self, other):

        if self.A.ccw(self.B, other.A) * self.A.ccw(self.B, other.B) > 0:
            return False
        if other.A.ccw(other.B, self.A) * other.A.ccw(other.B, self.B) > 0:
            return False
        return True

    def is_parallel(self, other):

        return not self.intersects(other)

    def is_colinear(self, other):

        return all([other.A in self, other.B in self])

    def intersection(self, other):

        if self.is_colinear(other):
            raise ValueError(f'{other} and {self} are colinear')

        if self.is_parallel(other):
            raise ValueError('{other} and {self} are parallel')

        d0 = self.A - self.B
        d1 = other.A - other.B
        denominator = (d0.x * d1.y) - (d0.y * d1.x)
        cp0 = self.A.cross(self.B)
        cp1 = other.A.cross(other.B)

        x_val = (cp0 * d1.x) - (d0.x * cp1) / denominator
        y_val = (cp0 * d1.y) - (d0.y * cp1) / denominator
        p = Point(x_val, y_val)

        if p in self and p in other:
            return p

        raise ValueError(f'calculated point {p} not in {self} and {other}')


    def distance_from_point(self, point):

        d = self.m
        n = (d.y * point.x) - (d.x * point.y) + self.A.cross(self.B)
        return abs(n / self.A.distance(self.B))

    def is_normal(self, other):

        return math.isclose(abs(self.degrees_between(other)), 90.0)

    def radians_between(self, other):

        a = Point.unit(self.A, self.B)
        b = Point.unit(other.A, other.B)
        return math.acos(a.dot(b))


class Ray(Line):
    pass


class Segment(Line):

    @property
    def length(self):
        return self.A.distance(self.B)
