import math
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def draw(self, color):
        pass


class Circle(Figure):
    def __init__(self, center, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive value")

        self.center = center
        self.radius = radius

    def draw(self, color):
        print(f"Drawing Circle: {self.center} with radius {self.radius} in color {color}")

    def __str__(self):
        return f"Circle: Center={self.center}, Radius={self.radius}"


class Triangle(Figure):
    def __init__(self, vertices):
        if len(vertices) != 3:
            raise ValueError("Triangle must have exactly 3 vertices")

        self.vertices = vertices

        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle")

    def is_valid_triangle(self):
        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        a = distance(self.vertices[0], self.vertices[1])
        b = distance(self.vertices[1], self.vertices[2])
        c = distance(self.vertices[2], self.vertices[0])

        return a + b > c and b + c > a and c + a > b

    def draw(self, color):
        print(f"Drawing Triangle: {self.vertices} in color {color}")

    def __str__(self):
        return f"Triangle: Vertices={self.vertices}"


class Rectangle(Figure):
    def __init__(self, top_left, width, height):
        self.top_left = top_left
        self.width = width
        self.height = height

        if not self.is_valid_rectangle():
            raise ValueError("Invalid rectangle")

    def is_valid_rectangle(self):
        return self.width > 0 and self.height > 0

    def draw(self, color):
        print(f"Drawing Rectangle: {self.top_left}, width {self.width}, height {self.height} in color {color}")

    def __str__(self):
        return f"Rectangle: Top Left={self.top_left}, Width={self.width}, Height={self.height}"
