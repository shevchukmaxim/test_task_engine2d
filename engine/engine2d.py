from typing import Union

from engine.figures import Circle, Triangle, Rectangle


class Engine2D:
    def __init__(self):
        self._canvas = []
        self._color = "White"

    def add_figure(self, figure: Union[Circle, Triangle, Rectangle]) -> None:
        if not isinstance(figure, (Circle, Triangle, Rectangle)):
            raise TypeError("Unsupported figure type")
        self._canvas.append(figure)

    def get_canvas(self) -> list:
        return self._canvas

    def set_color(self, color: str) -> None:
        self._color = color

    def get_current_color(self) -> str:
        return self._color

    def draw(self) -> None:
        if self._canvas:
            for figure in self._canvas:
                figure.draw(self._color)
            self._canvas = []  # Cleaning the canvas after drawing
        else:
            print("Canvas is empty. Add some figures to draw")
