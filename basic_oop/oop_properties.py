import math


class Point:
    """Point class

    Attributes
    ----------
    self.x : float
        x coordinate

    self.y : float
        y coordinate
    """

    def __init__(self, x, y):
        """Initialization

        Initialize point in 2 dimensional space.

        :param x: x coordinate
        :type x: float
        :param y: y coordinate
        :type y: float
        """

        self._x = x
        self._y = y

    @property
    def x(self):
        """Get x coordinate

        :return: x coordinate
        :rtype: float
        """

        if not self._x:
            raise ValueError("Set non-empty x coordinate")

        if isinstance(self._x, str):
            return float(self._x)

        else:
            return self._x

    @x.setter
    def x(self, value):
        """Set value

        Set x coordinate

        :param value: x coordinate
        :type value: float
        """

        self._x = value

    def _get_y(self):
        """Get y coordinate

        :return: y coordinate
        :rtype: float
        """

        if not self._y:
            raise ValueError("Set non empty y value")

        if isinstance(self._y, str):
            return float(self._y)

        return self._y

    def _set_y(self, value):
        """Set value

        Set y coordinate

        :param value: y coordinate
        :type value: float
        """

        self._y = value

    y = property(_get_y, _set_y)

    def distance(self, p2):
        """Compute distance

        Compute Euclidean distance between two points.

        :param p2: point 2
        :type p2: Point
        :return: distance between point 2 and the current point
        :rtype: float
        """

        return math.sqrt((self.x - p2.x)**2 + (self.y - p2.y)**2)


class Polygon:
    """Polygon class

    Attributes
    ----------
    self.vertices : list of Point
        vertices of a polygon
    """

    def __init__(self):
        self.vertices = []

    def add_point(self, point):
        """Add point

        Add point to create the vertices of the polygon

        :param point: polygon vertex
        :type point: Point
        """

        self.vertices.append(point)

    def perimeter(self):
        """Compute perimeter

        Compute the perimeter of the polygon.

        :return: sum of all sides of the polygon
        :rtype: float
        """

        if not self.vertices:
            raise ValueError("Add points before computing the perimeter of the shape")

        perimeter = 0
        points = self.vertices + [self.vertices[0]]

        for i in range(len(self.vertices)):
            perimeter += points[i].distance(points[i+1])

        return perimeter


class Foo:
    @property
    def foo(self):
        if not hasattr(self, '_foo'):
            raise ValueError("Empty field - first define before accessing")

        return self._foo

    @foo.setter
    def foo(self, value):
        self._foo = value


if __name__ == "__main__":
    square = Polygon()

    p1 = Point('1', '1')
    p1.y = "1"

    square.add_point(p1)
    square.add_point(Point(1, 2))
    square.add_point(Point(2, 2))
    square.add_point(Point(2, 1))

    print(square.perimeter())

    f = Foo()
    f.foo = "bar"
    print(f.foo)


