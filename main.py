from engine.engine2d import Engine2D
from engine.figures import Circle, Triangle, Rectangle


if __name__ == '__main__':
    engine = Engine2D()

    circle = Circle((0, 1), 5)
    triangle = Triangle([(0, 0), (1, 0), (0.5, 1)])
    rectangle = Rectangle((1, 1), 2, 3)

    engine.add_figure(circle)
    engine.add_figure(triangle)
    engine.add_figure(rectangle)

    engine.set_color("yellow")
    engine.draw()
    engine.set_color("red")
    engine.add_figure(rectangle)
    engine.draw()

