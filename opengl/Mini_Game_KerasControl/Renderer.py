import numpy as np
from glumpy import gloo, app, gl, glm
import Environment as env


# Create window with valid GL context
window = app.Window(width=1024, height=1024, color=(1, 1, 1, 1))


Environment = env()


@window.event
def on_draw(dt):
    window.clear()
    player.update_position()
    player.Obj.draw(gl.GL_TRIANGLE_STRIP)
