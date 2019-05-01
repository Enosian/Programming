import numpy as np
from glumpy import gloo, app, gl, glm

# Make a vertex with adjustable position
vertex = """
    attribute vec2 position;

    void main(){
                gl_PointSize = 5.0;
                gl_Position = vec4(position, 0.0, 1.0);
                } """

fragment = """
  uniform vec4 color;

  void main() {
      gl_FragColor = color;
  }
  """

# Create window with valid GL context
window = app.Window(height=1024, width=1024)

# Build the programm and corresponding buffers (with 4 vertices)
points = gloo.Program(vertex, fragment)

# Set Grid size to 1/10
grid_spacing = {x / 10 for x in range(10)}


def adjust_position(direction):
    x, y = 0, 0
    points['position'] = (x + 0.9, y + 1.0)

    class step_size:
        def __iter__(self):
            self.a = -1
            return self

        def __next__(self):
            x = self.a
            self.a += 0.1
            return x
    if direction == "w" and y < 0:
        y += 0.1
    if direction == "s" and y > -2:
        y -= 0.1
    if direction == "a" and x > -2:
        x -= 0.1
    if direction == "d" and x < 0:
        x += 0.1


points['color'] = 1, 1, 0, 1
points['position'] = (0.9, 1.0)


@window.event
def on_draw(dt):
    window.clear()
    points.draw(gl.GL_POINTS)


# Dictionary of keys
Keys = {
    87: "w",
    65: "a",
    83: "s",
    68: "d"
}


# @window.event
# def on_key_press(symbol, modifiers):
#     adjust_position(Keys[symbol])
#     print(Keys[symbol])


app.run()
