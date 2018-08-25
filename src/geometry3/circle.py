'''
'''

from dataclasses import dataclass
from .point import Point
from .line import Segment
import math


@dataclass
class Ellipse:
    center: Point = (0, 0, 0)
    radius: Point = (1, 0, 0)

    def __hash__(self):
        return hash(self.center) + hash(self.radius)

    @property
    def major_radius(self):
        return max(self.radius.x, self.radius.y)

    @property
    def minor_radius(self):
        return max(self.radius.x, self.radius.y)

    @property
    def x_is_major_axis(self):
        return self.major_radius == self.radius.x

    @property
    def x_is_minor_axis(self):
        return self.minor_radius == self.radius.x

    @property
    def y_is_major_axis(self):
        return self.major_radius == self.radius.y

    @property
    def y_is_minor_axis(self):
        return self.minor_radius == self.radius.y

    @property
    def eccentricity(self):
        '''
        The ratio of the distance between the two foci to the length
        of the major axis, float.

        0 <= e <= 1

        An eccentricity of zero indicates the ellipse is a circle.

        As e tends towards 1, the ellipse elongates.  It tends to the
        shape of a line segment if the foci remain a finite distance
        apart and a parabola if one focus is kept fixed as the other
        is allowed to move arbitrarily far away.

        '''
        return math.sqrt(1 - ((self.minor_radius / self.major_radius) ** 2))

    @property
    def linear_eccentricity(self):
        '''
        Distance between the center of the ellipse and a focus, float.

        '''
        return math.sqrt((self.major_radius ** 2) - (self.minor_radius ** 2))

    @property
    def a(self):
        '''
        Positive antipodal point on the major axis, Point class.

        '''
        a = Point.fromPoint(self.center)

        if self.x_is_major_axis:
            a.x += self.major_radius
        else:
            a.y += self.major_radius
        return a

    @property
    def a_neg(self):
        '''
        Negative antipodal point on the major axis, Point class.

        '''
        na = Point.fromPoint(self.center)

        if self.x_is_major_axis:
            na.x -= self.major_radius
        else:
            na.y -= self.major_radius
        return na

    @property
    def b(self):
        '''
        Positive antipodal point on the minor axis, Point class.

        '''
        b = Point.fromPoint(self.center)

        if self.x_is_minor_axis:
            b.x += self.minor_radius
        else:
            b.y += self.minor_radius
        return b

    @property
    def b_neg(self):
        '''
        Negative antipodal point on the minor axis, Point class.
        '''
        nb = Point.fromPoint(self.center)

        if self.x_is_minor_axis:
            nb.x -= self.minor_radius
        else:
            nb.y -= self.minor_radius
        return nb

    @property
    def focus0(self):
        '''
        First focus of the ellipse, Point class.

        '''
        f = Point.fromPoint(self.center)

        if self.x_is_major_axis:
            f.x -= self.linear_eccentricity
        else:
            f.y -= self.linear_eccentricity
        return f

    @property
    def f0(self):
        '''
        Shorthand notation for focus0, Point class
        '''
        return self.focus0

    @property
    def focus1(self):
        '''
        Second focus of the ellipse, Point class.
        '''
        f = Point.fromPoint(self.center)

        if self.x_is_major_axis:
            f.x += self.linear_eccentricity
        else:
            f.y += self.linear_eccentricity
        return f

    @property
    def f1(self):
        '''
        Shorthand notation for focus1, Point class
        '''
        return self.focus1

    @property
    def foci(self):
        '''
        A list containing the ellipse's foci, list.

        '''
        return [self.focus0, self.focus1]

    @property
    def major_axis(self):

        return Segment(self.a_neg, self.a)

    @property
    def minor_axis(self):
        return Segment(self.b_neg, self.b)

    @property
    def is_circle(self):
        return self.radius.x == self.radius.y

    def __eq__(self, other):

        return self.center == self.other and self.radius == other.radius

    def __contains__(self, point):

        d = sum(point.distance(f) for f in self.foci)
        # d < majorAxis.length interior point
        # d == majorAxis.length on perimeter of ellipse
        # d > majorAxis.length exterior point
        return d <= self.major_axis.length


@dataclass
class Circle:
    radius: float = 1

    def __contains__(self, point):

        return point.distance(self.center) <= self.radius

    def __hash__(self):

        return hash(self.center) + hash(bytes(self.radius))

    @property
    def diameter(self):

        return self.radius * 2

    @property
    def circumfrence(self):

        return 2 * math.pi * self.radius

    @property
    def area(self):

        return math.pi * (self.radius ** 2)
