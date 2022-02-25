import math

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
    pass


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
    return 0.0

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
    return 0.0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
