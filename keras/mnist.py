import    # ----------------------------------------------
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
