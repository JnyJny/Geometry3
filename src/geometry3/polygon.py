'''
'''

from .point import ColinearPoints


class Polygon:

    def __contains__(self, point):

        try:
            r = [p.is_ccw(q, point) for p, q in self.edges]
        except ColinearPoints:
            return True
        return not (any(r) and not all(r))

    @property
    def edges(self):

        if len(self.vertices) <= 1:
            raise ValueError('Not enough points in polygon')

        return [(p, q) for p, q in zip(self.vertices, self.vertices[1:])]

    @property
    def midpoints(self):

        return [p.midpoint(q) for p, q in self.edges]

    @property
    def sides(self):

        return [p.distance(q) for p, q in self.edges]

    @property
    def perimiter(self):

        return sum(self.sides)

    @property
    def semipeirmiter(self):

        return self.perimiter / 2

    @property
    def centroid(self):

        return sum(self.vertices) / len(self.vertices)

    @property
    def incenter(self):
        '''
        The intersection of angle bisectors, Point.

        '''
        n = len(self.vertices)
        return sum([s * p for s, p in zip(self.sides, self.vertices)]) / n
