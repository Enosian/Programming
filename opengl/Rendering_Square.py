from glumpy import app, gloo, gl

vertex = """
    attribute vec2 position;

    void main(){
                gl_Position = vec4(position, 0.0, 1.0);
                } """

fragment = """
  uniform vec4 color;

  void main() {
      gl_FragColor = color;
  }
  """

# Create window with valid GL context
window = app.Window(width=1024, height=1024, color=(1, 1, 1, 1))

# Build the programm and corresponding buffers (with 4 vertices)
quad = gloo.Program(vertex, fragment, count=4)

# Upload data into the GPU
quad['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)
quad['color'] = 1, 1, 0, 1
# Tell glumpy what needs to be done at each redraw

d = 1
step = 1 / 60


@window.event
def on_draw(dt):
    global d, step
    window.clear()
    quad.draw(gl.GL_TRIANGLE_STRIP)
    quad['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)



# Run the app
app.run()
