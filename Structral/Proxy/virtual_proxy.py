class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f'Loading the file {filename}')

    def draw(self):
        print(f'Drawing image {self.filename}')


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def _load_bitmap(self):
        if self._bitmap is None:
            self._bitmap = Bitmap(self.filename)

    def draw(self):
        self._load_bitmap()
        self._bitmap.draw()


def draw_image(bitmap):
    print('About to draw')
    bitmap.draw()
    print('Done drawing the image\n')


if __name__ == '__main__':
    bitmap = Bitmap('dog.jpg')
    draw_image(bitmap)

    lazy_bitmap = LazyBitmap('dog.jpg')
    draw_image(lazy_bitmap)

    draw_image(lazy_bitmap)
