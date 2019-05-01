import numpy as np
from glumpy import gloo, app, gl, glm
from Player import Pixel
from Trap import Enemy_Trap
import Environment as env


# Create window with valid GL context
window = app.Window(width=1024, height=1024, color=(1, 1, 1, 1))


player = Pixel()


@window.event
def on_draw(dt):
    window.clear()
    player.update_position()
    player.Obj.draw(gl.GL_TRIANGLE_STRIP)
    render_queue(env.Objects["Traps"])


def render_queue(queue):
    for ellement in queue:
        currEllem = Enemy_Trap(ellement[0], ellement[1], ellement[2], ellement[3])
        currEllem.Obj.draw(gl.GL_TRIANGLE_STRIP)



# Dictionary of keys
Keys = {
    87: "w",
    65: "a",
    83: "s",
    68: "d"
}


@window.event
def on_key_press(symbol, modifiers):
    player.shift_position(Keys[symbol])


# add_to_queue((10, (15, 20), 1, 5))

app.run()
