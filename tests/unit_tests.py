import pytest

from engine.figures import Circle, Triangle, Rectangle

FIGURES = [
    Circle((0, 1), 5),
    Triangle([(0, 0), (1, 0), (0.5, 1)]),
    Rectangle((1, 1), 2, 3)
]


@pytest.mark.parametrize("figure", FIGURES)
def test_engine_add_figure(engine, figure):
    engine.add_figure(figure)
    assert figure in engine.get_canvas()


def test_engine_add_invalid_figure(engine):
    with pytest.raises(TypeError) as exc_info:
        engine.add_figure('test')

    assert str(exc_info.value) == 'Unsupported figure type'


def test_engine_set_color(engine, expected_color="Red"):
    engine.set_color(expected_color)
    assert engine.get_current_color() == expected_color


def test_engine_draw_single_shape(engine, capfd):
    circle = Circle((0, 1), 5)
    engine.add_figure(circle)
    engine.draw()

    captured = capfd.readouterr()
    output = captured.out.strip().split('\n')

    assert output[0] == "Drawing Circle: (0, 1) with radius 5 in color White"


def test_engine_draw_multiple_shapes(engine, capfd):
    circle, triangle, rectangle = FIGURES

    engine.add_figure(circle)
    engine.add_figure(triangle)
    engine.add_figure(rectangle)
    engine.draw()

    captured = capfd.readouterr()
    output = captured.out.strip().split('\n')

    assert output[0] == "Drawing Circle: (0, 1) with radius 5 in color White"
    assert output[1] == "Drawing Triangle: [(0, 0), (1, 0), (0.5, 1)] in color White"
    assert output[2] == "Drawing Rectangle: (1, 1), width 2, height 3 in color White"


def test_engine_draw_multiple_shapes_with_different_colors(engine, capfd):
    circle, triangle, rectangle = FIGURES

    engine.add_figure(circle)
    engine.set_color("Green")
    engine.draw()
    engine.add_figure(triangle)
    engine.set_color("Red")
    engine.draw()
    engine.add_figure(rectangle)
    engine.set_color("Blue")
    engine.draw()

    captured = capfd.readouterr()
    output = captured.out.strip().split('\n')

    assert output[0] == "Drawing Circle: (0, 1) with radius 5 in color Green"
    assert output[1] == "Drawing Triangle: [(0, 0), (1, 0), (0.5, 1)] in color Red"
    assert output[2] == "Drawing Rectangle: (1, 1), width 2, height 3 in color Blue"


def test_engine_draw_empty_canvas(engine, capfd):
    assert engine.get_canvas() == []

    engine.draw()

    captured = capfd.readouterr()
    output = captured.out.strip().split('\n')

    assert output[0] == "Canvas is empty. Add some figures to draw"


def test_figure_circle_create():
    circle_coordinates = (0, 1)
    circle_radius = 5

    circle = Circle(circle_coordinates, circle_radius)

    assert str(circle) == f"Circle: Center={circle_coordinates}, Radius={circle_radius}"


def test_figure_circle_create_with_invalid_radius():
    circle_coordinates = (0, 1)
    circle_radius = -1

    with pytest.raises(ValueError) as exc_info:
        Circle(circle_coordinates, circle_radius)

    assert str(exc_info.value) == 'Radius must be a positive value'


def test_figure_triangle_create():
    triangle_vertices = [(0, 0), (1, 0), (0.5, 1)]

    triangle = Triangle(triangle_vertices)

    assert str(triangle) == f"Triangle: Vertices={triangle_vertices}"


def test_figure_triangle_create_with_invalid_number_of_vertices():
    triangle_vertices = [(0, 0), (1, 0)]

    with pytest.raises(ValueError) as exc_info:
        Triangle(triangle_vertices)

    assert str(exc_info.value) == 'Triangle must have exactly 3 vertices'


def test_figure_triangle_create_with_invalid_vertices():
    triangle_vertices = [(0, 0), (1, 0), (1, 0)]

    with pytest.raises(ValueError) as exc_info:
        Triangle(triangle_vertices)

    assert str(exc_info.value) == 'Invalid triangle'


def test_figure_rectangle_create():
    top_left_coordinate = (1, 1)
    width = 2
    height = 3

    rectangle = Rectangle(top_left_coordinate, width, height)

    assert str(rectangle) == f"Rectangle: Top Left={top_left_coordinate}, Width={width}, Height={height}"


def test_figure_rectangle_create_with_invalid_width():
    top_left_coordinate = (1, 1)
    width = -1
    height = 3

    with pytest.raises(ValueError) as exc_info:
        Rectangle(top_left_coordinate, width, height)

    assert str(exc_info.value) == 'Invalid rectangle'


def test_figure_rectangle_create_with_invalid_height():
    top_left_coordinate = (1, 1)
    width = 3
    height = -1

    with pytest.raises(ValueError) as exc_info:
        Rectangle(top_left_coordinate, width, height)

    assert str(exc_info.value) == 'Invalid rectangle'


def test_figure_draw(capfd):
    circle, triangle, rectangle = FIGURES

    circle.draw("red")
    triangle.draw("blue")
    rectangle.draw("green")

    captured = capfd.readouterr()
    output = captured.out.strip().split('\n')

    assert output[0] == "Drawing Circle: (0, 1) with radius 5 in color red"
    assert output[1] == "Drawing Triangle: [(0, 0), (1, 0), (0.5, 1)] in color blue"
    assert output[2] == "Drawing Rectangle: (1, 1), width 2, height 3 in color green"
