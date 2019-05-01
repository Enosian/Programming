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


# Tell glumpy what needs to be done at each redraw
green = 1


def color_shift():
  global green
  red = 1 - green
  quad['color'] = red, green, 0, 1
  green -= .005


@window.event
def on_draw(dt):
  global d, step
  window.clear()
  quad.draw(gl.GL_TRIANGLE_STRIP)
  quad['position'] = (-1, +1), (+1, +1), (-1, -1), (+1, -1)
  color_shift()
# Run the app


app.run()
