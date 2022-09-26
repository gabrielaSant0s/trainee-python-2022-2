
class Point():
    """
    A two-dimensional Point with an x and an y value
    >>> Point(0.0, 0.0)
    Point(0.0, 0.0)
    >>> Point(1.0, 0.0).x
    1.0
    >>> Point(0.0, 2.0).y
    2.0
    >>> Point(y = 3.0, x = 1.0).y
    3.0
    >>> Point(1, 2)
    Traceback (most recent call last):
        ...
    ValueError: both coordinates value must be float
    >>> a = Point(0.0, 1.0)
    >>> a.x
    0.0
    >>> a.x = 3.0
    >>> a.x
    3.0
    """
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self.float_coordinate()

    def float_coordinate(self):
        if type(self.x) != float or type(self.y) != float:
            raise ValueError("both coordinates value must be float")

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self,x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,y):
        self._y = y

    def __repr__(self) -> str:
        return f'Point({self._x}, {self._y})'

def euclidean_distance(a, b):
    """
    Returns the euclidean distance between Point a and Point b
    >>> euclidean_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    5.0
    >>> euclidean_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> euclidean_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """
    if type(a) != Point:
        raise ValueError('a must be a Point')
    elif type(b) != Point:
        raise ValueError('b must be a Point')
    
    distance = ((b.x - a.x)**2+(b.y - a.y)**2)**(1/2)

    return distance

def manhattan_distance(a, b):
    """
    Returns the manhattan distance between Point a and Point b
    >>> manhattan_distance(Point(0.0, 0.0), Point(3.0, 4.0))
    7.0
    >>> manhattan_distance((0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: a must be a Point
    >>> manhattan_distance(Point(0.0, 0.0), (3.0, 4.0))
    Traceback (most recent call last):
        ...
    ValueError: b must be a Point
    """
    if type(a) != Point:
        raise ValueError('a must be a Point')
    elif type(b) != Point:
        raise ValueError('b must be a Point')
    
    distance = ((a.x - b.x)**2)**(1/2) + ((a.y - b.y)**2)**(1/2)
    return distance

if __name__ == "__main__":
    import doctest
    doctest.testmod()
