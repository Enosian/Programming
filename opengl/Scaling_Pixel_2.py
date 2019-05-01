import numpy as np
from glumpy import gloo, app, gl, glm

# Vertex Shader
vertex = """
  attribute vec2 position;
  void main() {
      gl_Position = vec4(position, 0.0, 1.0);
  } """

# Fragment Shader
fragment = """
    void main() {
        gl_FragColor = vec4(vec3(0.0), 1.0);
    }"""

# Create window with valid GL context
window = app.Window(width=1024, height=1024, color=(1, 1, 1, 1))

# Build the programm and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)


# position_manager(key):
#     -check for out of bounds positions
#     -shift coordinates

class position_manager:
    dx, dy = 0, 0
    position = {}

    def shift_position(self, key):
        if key == "w" and self.position[1] != 1:
            self.dy += 0.1
        if key == "s"and self.position[1] != -0.9:
            self.dy -= 0.1
        if key == "a" and self.position[0] != -1:
            self.dx -= 0.1
        if key == "d" and self.position[0] != 1:
            self.dx += 0.1

    def update_position(self):
        quad["position"] = (-1 + self.dx, -0.9 + self.dy), (-0.9 + self.dx, -0.9 + self.dy), (-1 + self.dx, -1 + self.dy), (-0.9 + self.dx, -1 + self.dy)

        self.position = (-1 + self.dx, -0.9 + self.dy)

    def __init__(self):
        self.update_position()


manager = position_manager()


@window.event
def on_draw(dt):
    window.clear()
    manager.update_position()
    quad.draw(gl.GL_TRIANGLE_STRIP)


# Dictionary of keys
Keys = {
    87: "w",
    65: "a",
    83: "s",
    68: "d"
}


@window.event
def on_key_press(symbol, modifiers):
    manager.shift_position(Keys[symbol])


app.run()
