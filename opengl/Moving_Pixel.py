import numpy as np
from glumpy import app, gl, glm, gloo

vertex = """
  attribute vec2 position;
  void main() {
      gl_PointSize = 10.0;
      gl_Position = vec4(position, 0.0, 1.0);
  } """

fragment = """
    void main() {
        gl_FragColor = vec4(vec3(0.0), 1.0);
    } """

window = app.Window(width=512, height=512, color=(1, 1, 1, 1))
points = gloo.Program(vertex, fragment, count=1000)


step = 1 / 100
init = np.array([1, 1], dtype=np.float32)


@window.event
def on_draw(dt):
    global step
    window.clear()
    points["position"] = [init[0], init[1]]
    points.draw(gl.GL_POINTS)

    if init[0] > -1:
        init[0] -= step
        print(init[0])

    else:
        init[1] -= 0.01
        step *= -1
        init[0] -= step

    if init[0] == 1:
        print(init[0])
        init[1] -= 0.01
        step *= -1
        init[0] -= step


app.run(framerate=60)
