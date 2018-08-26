import pytest
from geometry3 import Point


@pytest.fixture
def ORIGIN():
    return Point()


@pytest.fixture
def ONES():
    return Point(1, 1, 1)


@pytest.fixture
def UNITS():
    return Point.units()


@pytest.fixture
def point():
    return Point()


def point_equals(p, x, y, z):
    return all([p.x == x, p.y == y, p.z == z, p.w == 1])

class TestPoint:
    
    def is_zero(self, ORIGIN):
        assert point_equals(ORIGIN, 0, 0, 0)
        assert ORIGIN.is_origin is True


    def can_set_x_y_z(self, ORIGIN):
        ORIGIN.x = 1
        ORIGIN.y = 1
        ORIGIN.z = 1
        assert ORIGIN.x != 0 and ORIGIN.x == 1
        assert ORIGIN.y != 0 and ORIGIN.y == 1
        assert ORIGIN.z != 0 and ORIGIN.z == 1


    def can_set_xy(self, ORIGIN):
        ORIGIN.xy = 1, 2
        assert point_equals(ORIGIN, 1, 2, 0)


    def can_set_xyz(self, ORIGIN):
        ORIGIN.xyz = 1, 2, 3
        assert point_equals(ORIGIN, 1, 2, 3)


    def can_set_xyzw(self, ORIGIN):
        ORIGIN.xyzw = 1, 2, 3, 4
        assert point_equals(ORIGIN, 1, 2, 3)


    def verify_units(self, UNITS):
        i, j, k = UNITS
        assert point_equals(i, 1, 0, 0)
        assert point_equals(j, 0, 1, 0)
        assert point_equals(k, 0, 0, 1)


    def is_not_origin(self, ONES):
        assert point_equals(ONES, 1, 1, 1)
        assert ONES.is_origin is not True


    def check_iter(self, point):
        point.xyz = 0, 1, 2
        for i, v in enumerate(point):
            assert v == i


    def verify_add(self, UNITS, ONES):
        i, j, k = UNITS
        assert sum(UNITS) == ONES
        assert point_equals(i + j, 1, 1, 0)
        assert point_equals(j + i, 1, 1, 0)
        assert point_equals(i + 1, 2, 1, 1)
        assert point_equals(1 + i, 2, 1, 1)
        k += 1
        assert point_equals(k, 1, 1, 2)
        k += j
        assert point_equals(k, 1, 2, 2)



    def verify_sub(self, UNITS):
        i, j, k = UNITS
        assert point_equals(i - j, 1, -1, 0)
        assert point_equals(j - i, -1, 1, 0)
        assert point_equals(i - 1, 0, -1, -1)
        assert point_equals(1 - i, 0, -1, -1)
        k -= 1
        assert point_equals(k, -1, -1, 0)
        k -= j
        assert point_equals(k, -1, -2, 0)


    def verify_mul(self, UNITS):
        i, j, k = UNITS
        assert (i * j).is_origin
        assert (j * i).is_origin
        assert (i * j * k).is_origin
        assert (j * 1) == j
        assert (1 * j) == j
        assert (j * 0).is_origin
        assert (0 * j).is_origin
        i *= 2
        assert point_equals(i, 2, 0, 0)
        i *= j
        assert i.is_origin

    
    def verify_truediv(self, UNITS):
        pass


    def verify_floordiv(self, UNITS):
        pass


    def verify_pow(self, ONES):
        pass


    def verify_pos_neg(self, ORIGIN):
        pass


    def verify_abs(self, ORIGIN):
        pass


    def verify_invert(self, ORIGIN):
        pass


    def verify_distance(self, UNITS):
        i, j, k = UNITS
        assert i.distance() == 1
        assert j.distance() == 1
        assert k.distance() == 1
        assert i.distance(j) == j.distance(i)
        assert i.distance(k) == k.distance(i)
        assert j.distance(k) == k.distance(j)


    def verify_ccw(self, UNITS):
        i, j, k = UNITS

    def verify_is_ccw(self, UNITS):
        i, j, k = UNITS

    def verify_is_colinear(self, UNITS):
        i, j, k = UNITS

    def verify_midway(self, ONES, ORIGIN):
        assert point_equals(ONES.midpoint(), .5, .5, .5)
        assert ONES.midpoint(ORIGIN) == ORIGIN.midpoint(ONES)
