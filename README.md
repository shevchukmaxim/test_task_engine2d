### Task
Implement a 2D engine that can "draw" basic 2D primitives on the screen. The engine itself should be represented as an object of the Engine2D class.
- The engine should have a "canvas" and the ability to add shapes to it. The canvas will contain the current list of primitives to be drawn.
- Implement classes for three geometric shapes: circle, triangle, and rectangle. Choose the necessary parameters for creating the shapes yourself.
- Each shape should have a draw() method that prints information, for example, "Drawing Circle: (0, 1) with radius 5", when called.
- When finished adding shapes, the engine should call a public draw() method that sequentially calls the draw() methods of all the shapes on the canvas and clears it.
- Add the ability to change the drawing color by calling a public method on the engine (think of it as "changing the pencil"):
- After calling this method, all subsequent shapes should be drawn in the specified color until a new color is set.
- The color with which a shape will be drawn should be displayed in the drawing text.
- Write unit tests using pytest. Determine the required number of tests on your own.
### Install
```console
python -m pip install -r requirements.txt
```

### How to run
To run this project run this command:

```console
 pytest tests/unit_tests.py 
 ```
