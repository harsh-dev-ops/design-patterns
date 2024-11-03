from abc import ABC


class Shape(ABC):
    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius=0.0):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor
        return self.radius

    def __str__(self):
        return f'Circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side=0.0):
        self.side = side

    def __str__(self):
        return f'Square of side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply ColoredDecorator twice')
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} has the color {self.color}'


class TransparentShape(Shape):
    def __init__(self, colored_shape, transparency):

        if isinstance(colored_shape, TransparentShape):
            raise Exception('Cannot apply TransparentDecorator twice')

        if not isinstance(colored_shape, ColoredShape):
            raise Exception(f'Only Colored Shape supported')

        self.shape = colored_shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100}% transparency'


if __name__ == "__main__":
    circle = Circle(5)
    print(circle)

    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    red_tranparent_circle = TransparentShape(red_circle, 0.3)
    print(red_tranparent_circle)
