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


def test_point_zero(ORIGIN):
    assert point_equals(ORIGIN, 0, 0, 0)
    assert ORIGIN.is_origin is True


def test_point_set(ORIGIN):
    ORIGIN.x = 1
    ORIGIN.y = 1
    ORIGIN.z = 1
    assert ORIGIN.x != 0 and ORIGIN.x == 1
    assert ORIGIN.y != 0 and ORIGIN.y == 1
    assert ORIGIN.z != 0 and ORIGIN.z == 1


def test_point_set_xy(ORIGIN):
    ORIGIN.xy = 1, 2
    assert point_equals(ORIGIN, 1, 2, 0)


def test_point_set_xyz(ORIGIN):
    ORIGIN.xyz = 1, 2, 3
    assert point_equals(ORIGIN, 1, 2, 3)


def test_point_set_xyzw(ORIGIN):
    ORIGIN.xyzw = 1, 2, 3, 4
    assert point_equals(ORIGIN, 1, 2, 3)


def test_point_units(UNITS):
    i, j, k = UNITS
    assert point_equals(i, 1, 0, 0)
    assert point_equals(j, 0, 1, 0)
    assert point_equals(k, 0, 0, 1)


def test_point_not_origin(ONES):
    assert point_equals(ONES, 1, 1, 1)
    assert ONES.is_origin is not True


def test_point_iter(point):
    point.xyz = 0, 1, 2
    for i, v in enumerate(point):
        assert v == i


def test_point_add(UNITS):
    i, j, k = UNITS
    assert point_equals(i + j, 1, 1, 0)
    assert point_equals(j + i, 1, 1, 0)
    assert point_equals(i + 1, 2, 1, 1)
    assert point_equals(1 + i, 2, 1, 1)
    k += 1
    assert point_equals(k, 1, 1, 2)
    k += j
    assert point_equals(k, 1, 2, 2)


def test_point_sub(UNITS):
    i, j, k = UNITS
    assert point_equals(i - j, 1, -1, 0)
    assert point_equals(j - i, -1, 1, 0)
    assert point_equals(i - 1, 0, -1, -1)
    assert point_equals(1 - i, 0, -1, -1)
    k -= 1
    assert point_equals(k, -1, -1, 0)
    k -= j
    assert point_equals(k, -1, -2, 0)


def test_point_mul(UNITS):
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

    
def test_point_truediv(UNITS):
    pass


def test_point_floordiv(UNITS):
    pass


def test_point_pow(ONES):
    pass


def test_point_pos_neg(ORIGIN):
    pass


def test_point_abs(ORIGIN):
    pass


def test_point_invert(ORIGIN):
    pass


def test_point_distance(UNITS):
    i, j, k = UNITS
    assert i.distance() == 1
    assert j.distance() == 1
    assert k.distance() == 1
    assert i.distance(j) == j.distance(i)
    assert i.distance(k) == k.distance(i)
    assert j.distance(k) == k.distance(j)


def test_point_ccw(UNITS):
    i, j, k = UNITS

def test_point_is_ccw(UNITS):
    i, j, k = UNITS

def test_point_is_colinear(UNITS):
    i, j, k = UNITS

def test_point_midway(ONES, ORIGIN):

    assert point_equals(ONES.midpoint(), .5, .5, .5)
    assert ONES.midpoint(ORIGIN) == ORIGIN.midpoint(ONES)
