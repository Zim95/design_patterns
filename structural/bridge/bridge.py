from abc import ABC


class Renderer(ABC):

    def render_circle(self, radius):
        pass

    def render_square(self, size):
        pass


class VectorRenderer(Renderer):

    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):

    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:

    def __init__(self, renderer):
        self.renderer = renderer
    
    def draw(self): pass

    def resize(self, factor): pass


class Circle(Shape):

    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        super().draw()

    def resize(self, factor):
        self.radius *= factor
