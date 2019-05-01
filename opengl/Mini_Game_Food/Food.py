import numpy as np
from glumpy import app, gloo, gl

vertex = """
  attribute vec2 position;
  void main() {
      gl_PointSize = 20.0;
      gl_Position = vec4(position, 0.0, 1.0);
  } """

fragment = """
  void main() {
       gl_FragColor = vec4(vec3(0.0), 1.0);
  } """

filler_fragment = """
  void main() {
       gl_FragColor = vec4(vec3(1.0), 1.0);
  } """

window = app.Window(512, 512, color=(1, 1, 1, 1))
food = gloo.Program(vertex, fragment, count=5)
position = np.random.randint(-9, 10, (len(food), 2)) / 10
food["position"] = position

eaten_array = []


def if_eaten(eaten, p_position):
    if eaten:
        if len(eaten_array) != 0:
            print(eaten_array)
            for i in len(eaten_array):
                if p_position != eaten_array[i]:
                    continue
                    eaten_array.append(p_position)
                else:
                    break
        else:
            eaten_array.append(p_position)
            print("hi")


overdraw = gloo.Program(vertex, filler_fragment, count=len(eaten_array))
overdraw["position"] = eaten_array


@window.event
def on_draw(dt):
    if_eaten(True, position[1])
    window.clear()
    food.draw(gl.GL_POINTS)
    overdraw.draw(gl.GL_POINTS)


app.run()
