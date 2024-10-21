import copy
from unittest import TestCase


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def deep_copy(self):
        return copy.deepcopy(self)


class Evaluate(TestCase):
    def test_exercise(self):
        line1 = Line(
            Point(3, 3),
            Point(10, 10)
        )
        line2 = line1.deep_copy()
        line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

        self.assertEqual(3, line2.start.x)
        self.assertEqual(3, line2.start.y)
        self.assertEqual(10, line2.end.x)
        self.assertEqual(10, line2.end.y)


evaluate = Evaluate()

try:
    evaluate.test_exercise()
    print("PASSED")
except AssertionError as ae:
    print(f"{ae}")
    print("FAILED")
