from abc import ABC, abstractmethod


class CircleRenderer(ABC):
    @abstractmethod
    def render_circle(self, circle):
        pass


class SquareRenderer(ABC):
    @abstractmethod
    def render_square(self, side):
        pass


class TriangleRenderer(ABC):
    @abstractmethod
    def render_triangle(self, a, b, c):
        pass


class VectorCircleRenderer(CircleRenderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")


class VectorSquareRenderer(SquareRenderer):
    def render_square(self, side):
        print(f"Drawing a square of side {side}")


class VectorTriangleRenderer(TriangleRenderer):
    def render_triangle(self, a, b, c):
        print(f"Drawing a triangle of sides {a}, {b}, {c}")


class RasterCircleRenderer(CircleRenderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for circle of radius {radius}")


class RasterSquareRenderer(SquareRenderer):
    def render_square(self, side):
        print(f"Drawing pixels for square of side {side}")


class RasterTriangleRenderer(TriangleRenderer):
    def render_triangle(self, a, b, c):
        print(f"Drawing pixels for triangle of sides {a}, {b}, {c}")


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor: int | float):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer, side):
        super().__init__(renderer)
        self.side = side

    def draw(self):
        self.renderer.render_square(self.side)

    def resize(self, factor):
        self.side *= factor


class Triangle(Shape):
    def __init__(self, renderer, a, b, c):
        super().__init__(renderer)
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        self.renderer.render_triangle(self.a, self.b, self.c)

    def resize(self, factor):
        self.a *= factor
        self.b *= factor
        self.b *= factor


if __name__ == "__main__":
    vector_circle_renderer = VectorCircleRenderer()
    raster_circle_renderer = RasterCircleRenderer()
    circle = Circle(vector_circle_renderer, 5)
    circle = Circle(raster_circle_renderer, 100)

    circle.draw()
    circle.resize(2)
    circle.draw()
