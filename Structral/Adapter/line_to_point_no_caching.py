class Point:
    def __init__(self, x: float | int, y: float | int):
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end='')
# ^^ We are given the point api only

# We have to draw a rectangle using point api.


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x+width, y)))
        self.append(Line(Point(x+width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    _count = 0

    def __init__(self, line):
        super().__init__()
        self._count += 1
        print(f"{self._count}: Generating points for line "
              f"({line.start.x}, {line.start.y}) -> "
              f"({line.end.x}, {line.end.y})")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = max(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rectangles):
    for rectangle in rectangles:
        for line in rectangle:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
        print()


if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)
