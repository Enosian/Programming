from glumpy import gloo, gl, glm


class Pixel:
    # ----------------------------------------------
    #       DEFINING AND INITIALIZING PIXEL

    # Vertex Shader
    def get_vertex():
        vertex = """
          attribute vec2 position;
          void main() {
              gl_Position = vec4(position, 0.0, 1.0);
          } """
        return vertex

    # Fragment Shader
    def get_fragment():
        fragment = """
            uniform vec4 color;

            void main() {
                gl_FragColor = color;
            }
            """
        return fragment

    Obj = gloo.Program(get_vertex(), get_fragment(), count=4)

    # ----------------------------------------------
    #               MOVING PIXEL

    dx, dy = 0, 0
    position = ()
    collider = None

    def shift_position(self, key):
        try:
            if key == "w" and self.position[1] != 1 and self.position[1] < 1 and self.collider.check_collision(self.position[1] + 0.1):
                self.dy += 0.1
            if key == "s"and self.position[1] != -0.9 and self.position[1] > -0.9 and self.collider.check_collision(self.position[1] - 0.1):
                self.dy -= 0.1
            if key == "a" and self.position[0] != -1 and self.position[0] > -1 and self.collider.check_collision(self.position[0] - 0.1):
                self.dx -= 0.1
            if key == "d" and self.position[0] != 0.9 and self.position[0] < 0.9 and self.collider.check_collision(self.position[0] + 0.1):
                self.dx += 0.1
        except Exception:
            pass

    def update_position(self):
        self.Obj["position"] = (-1 + self.dx, -0.9 + self.dy), (-0.9 + self.dx, -0.9 + self.dy), (-1 + self.dx, -1 + self.dy), (-0.9 + self.dx, -1 + self.dy)

        self.position = (-1 + self.dx, -0.9 + self.dy)

    # ----------------------------------------------
    #             DAMAGE DETECTION

    hp = 100

    # Move Obj by -100, -100 on death or otherwise adjust hp
    def update_hp(self, damage):
        if self.hp - damage <= 0:
            self.dx, self.dy = -100, -100
        else:
            self.hp -= damage

    def update_color(self):
        green = self.hp / 100
        red = 1 - green
        self.Obj['color'] = red, green, 0, 1

    def __init__(self, p_collider):
        self.collider = p_collider
        self.update_position()
        self.update_color()
