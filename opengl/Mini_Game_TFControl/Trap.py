from glumpy import gloo, app, gl, glm


class Enemy_Trap:
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

    def position_transform(self, p_height, p_width, p_position):
        dx, dy = 0, 0

        # Transform Size
        width = p_width / 10
        height = p_height / 10

        # Transform Position
        position = (p_position[0], p_position[1])

        self.dx = -1 + position[0] / 10
        self.dy = -1 + position[1] / 10

        # Set Object
        self.Obj["position"] = (self.dx, self.dy - height), (self.dx - width, self.dy - height), (self.dx, self.dy), (self.dx - width, self.dy)

    def __init__(self, damage, position, width, height):
        self.position_transform(height, width, position)
        self.Obj["color"] = 0, 0, 0, 1
