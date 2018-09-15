'''
'''

from dataclasses import dataclass
import math
import operator
import random
import hashlib

_half_pi = math.pi / 2
_two_pi = math.pi * 2


class ColinearPoints(Exception):
    pass


@dataclass
class Point:
    x: float = 0
    y: float = 0
    z: float = 0
    w: float = 1

    @classmethod
    def fromPoint(cls, point):
        return cls(point.x, point.y, point.z)

    @classmethod
    def units(cls, scale=1):

        return cls(x=scale), cls(y=scale), cls(z=scale)

    @classmethod
    def unit(cls, p0, p1):

        return (p1 - p0) / p0.distance(p1)

    @classmethod
    def gaussian(cls, mu=0, sigma=1):

        return cls(random.gauss(mu, sigma),
                   random.gauss(mu, sigma),
                   random.gauss(mu, sigma))

    @classmethod
    def random(cls, origin=None, radius=1):

        p = origin or Point()
        r, u, v = (random.uniform(0, radius),
                   random.uniform(0, _two_pi),
                   random.uniform(-_half_pi, _half_pi))
        rcosv = r * math.cos(v)
        cosu, sinu, sinv = math.cos(u), math.sin(u), math.sin(v)
        p += rcosv * cosu, rcosv * sinu, radius * sinv
        return p

    @property
    def is_origin(self):
        return all(v == 0 for v in self)

    @property
    def xy(self):
        return self.x, self.y

    @xy.setter
    def xy(self, xy):
        self.x, self.y = xy[:2]

    @property
    def xyz(self):
        return self.x, self.y, self.z

    @xyz.setter
    def xyz(self, xyz):
        self.x, self.y, self.z = xyz[:3]

    @property
    def xyzw(self):
        return self.x, self.y, self.z, self.w

    @xyzw.setter
    def xyzw(self, xyzw):
        self.xyz = xyzw

    def __hash__(self):

        if self.is_origin:
            return 0

        return int(hashlib.sha1(bytes(self)).hexdigest(), 16)

    def _binary_(self, other, func, in_place=False):
        '''
        '''
        target = self if in_place else Point()
        try:
            target.xyz = [func(a, b) for a, b in zip(self, other)]
            return target
        except TypeError:
            pass

        target.xyz = [func(a, b) for a, b in zip(self, [other] * 3)]
        return target

    def _unary_(self, func):
        '''
        '''
        target = Point()
        target.xyz = [func(v) for v in self]
        return target

    def __iter__(self):
        '''
        '''
        return iter(self.xyz)

    def __add__(self, other):
        '''
        '''
        return self._binary_(other, operator.add)

    def __radd__(self, other):
        '''
        '''
        return self._binary_(other, operator.add)

    def __iadd__(self, other):
        '''
        '''
        return self._binary_(other, operator.add, in_place=True)

    def __sub__(self, other):
        '''
        '''
        return self._binary_(other, operator.sub)

    def __rsub__(self, other):
        '''
        '''
        return self._binary_(other, operator.sub)

    def __isub__(self, other):
        '''
        '''
        return self._binary_(other, operator.sub, in_place=True)

    def __mul__(self, other):
        '''
        '''
        return self._binary_(other, operator.mul)

    def __rmul__(self, other):
        '''
        '''
        return self._binary_(other, operator.mul)

    def __imul__(self, other):
        '''
        '''
        return self._binary_(other, operator.mul, in_place=True)

    def __floordiv__(self, other):
        '''
        '''
        return self._binary_(other, operator.floordiv)

    def __rfloordiv__(self, other):
        '''
        '''
        return self._binary_(other, operator.floordiv)

    def __ifloordiv__(self, other):
        '''
        '''
        return self._binary_(other, operator.floordiv, in_place=True)

    def __truediv__(self, other):
        '''
        '''
        return self._binary_(other, operator.truediv)

    def __rtruediv__(self, other):
        '''
        '''
        return self._binary_(other, operator.truediv)

    def __itruediv__(self, other):
        '''
        '''
        return self._binary_(other, operator.truediv, in_place=True)

    def __pow__(self, exponent):
        '''
        '''
        return self._binary_(exponent, operator.pow)

    def __ipow__(self, exponent):
        '''
        '''
        return self._binary_(exponent, operator.pow, in_place=True)

    def __pos__(self):
        '''
        '''
        return self

    def __neg__(self):
        '''
        '''
        return self._unary_(operator.neg)

    def __invert__(self):
        '''
        '''
        return self._unary_(operator.invert)

    def __abs__(self):
        '''
        '''
        return self._unary_(operator.abs)

    def distance(self, other=None):
        '''
        '''
        return math.sqrt(self.distance_squared(other or Point()))

    def distance_squared(self, other=None):
        '''
        '''
        return sum((((other or Point()) - self)**2))

    def dot(self, other):
        '''
        '''
        return sum((self * other))

    def cross(self, other):
        '''
        '''        
        return sum([(self.y * other.z) - (self.z * other.y),
                    (self.z * other.x) - (self.x * other.z),
                    (self.x * other.y) - (self.y * other.x)])
        
    

    def ccw(self, b, c, axis='z'):
        '''this function determines direction of rotation described by
        the angle b,self,c around the specified axis.

        > 0 : counter-clockwise
          0 : colinear
        < 0 : clockwise

        :param b:    point
        :param c:    point
        :param axis: string in "xXyYzZ"
        :return: float

        raises valueerror if axis is not in "xXyYzZ".
        '''

        bsuba = b - self
        csuba = c - self

        if axis in 'zZ':
            return (bsuba.x * csuba.y) - (bsuba.y * csuba.x)

        if axis in 'yY':
            return (bsuba.x * csuba.z) - (bsuba.z * csuba.x)

        if axis in 'xX':
            return (bsuba.y * csuba.z) - (bsuba.z * csuba.y)

        raise ValueError(f'invalid axis={axis}, not in "xXyYzZ"')

    def is_ccw(self, b, c, axis='z'):
        '''
        '''
        result = self.ccw(b, c, axis)
        if result == 0:
            raise ColinearPoints(b, self, c)
        return result > 0

    def is_colinear(self, b, c):
        '''
        '''
        return all(self.ccw(b, c, axis) == 0 for axis in 'xyz')

    def midpoint(self, other=None):
        '''
        '''
        return abs((self - (other or Point())) / 2)
