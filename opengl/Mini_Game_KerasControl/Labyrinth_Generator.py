import numpy as np
import random
import math
from glumpy import gloo

# Generate a maze using a randomized version of prims algorithm


class Prims_Maze:
    def __init__(self, grid):
        self.grid = np.array([grid[0], grid[1]])

        self.vertex1 = """
              attribute vec2 position;
              void main() {
                  gl_PointSize = 20.0;
                  gl_Position = vec4(position, 0.0, 1.0);
              } """

        self.vertex2 = """
              attribute vec2 position;
              void main() {
                  gl_PointSize = 5.0;
                  gl_Position = vec4(position, 0.0, 1.0);
              } """

        self.fragment = """
              void main() {
                   gl_FragColor = vec4(vec3(0.0), 1.0);
              } """

    def generate_maze(self, food_amount, labyrinth_iterations):

        self.prims_generate(labyrinth_iterations)
        self.food_generate(food_amount)

        # self.marked_vertex = self.convert_positions(self.marked_vertex)
        # self.food_vertex = self.convert_positions(self.food_vertex)

    def food_generate(self, ammount):
        self.food_vertex = self.pathed_vertex[random.randint(0, self.pathed_vertex.shape[0])]

    def prims_generate(self, iterations):
        self.pathed_vertex = np.array([int(self.grid[1] / 2), int(self.grid[0])])
        self.marked_vertex = np.array([self.pathed_vertex + [0, 1]])

        # marks new verticies for future use in paths and checks them for validity
        def mark_vertex(vertex):
            class Next_Vertex(Exception):
                pass

            # new verticies in grid
            new_marked_vertex = np.array([-100, -100])
            if vertex[1] + 1 <= self.grid[1]:
                n = np.array([vertex[0], vertex[1] + 1])
                new_marked_vertex = np.vstack((new_marked_vertex, n))
            if vertex[1] - 1 >= self.grid[0]:
                new_marked_vertex = np.vstack((new_marked_vertex, [vertex[0], vertex[1] - 1]))
            if vertex[0] + 1 <= self.grid[1]:
                new_marked_vertex = np.vstack((new_marked_vertex, [vertex[0] + 1, vertex[1]]))
            if vertex[0] - 1 >= 0:
                new_marked_vertex = np.vstack((new_marked_vertex, [vertex[0] - 1, vertex[1]]))

            t, new_marked_vertex, l = np.split(new_marked_vertex, [1, 4], axis=0)

            # test new vertecies for vailidity
            for x in new_marked_vertex:
                if len(self.marked_vertex.shape) != 1:
                    try:
                        for y in self.pathed_vertex:
                            if y.all == x.all:
                                print("whack hack")
                                raise Next_Vertex
                        for y in self.marked_vertex:
                            # checks if distance between vertecies is >= 2
                            if math.sqrt((y[0] - x[0])**2 + (y[1] - x[1])**2) < 1:
                                raise Next_Vertex
                            # if x[1] >= self.grid[0]:
                            #     print("my maker just messed up :/")
                            #     raise Next_Vertex
                        self.marked_vertex = np.vstack((self.marked_vertex, x))
                        print("i did it")
                    except Next_Vertex:
                        print("i didnt do it")
                else:
                    self.marked_vertex = np.vstack((self.marked_vertex, new_marked_vertex[x]))
            print(self.marked_vertex)

        def search_for_ellement(array, ellement):
            # print("array:", array, "ellement:", ellement)
            for x in range(array.shape[0]):
                # print("hallo", array[x])
                if ellement.all() == array[x].all():
                    print(x)
                    return x
                    break
                else:
                    raise Exception('ellement {} was not found.'.format(ellement))
        for k in range(iterations):
            if self.marked_vertex.shape[0] > 1:
                # print("hi", self.marked_vertex, "kk:", self.marked_vertex.shape[0])
                new_pathed_vertex = self.marked_vertex[random.randint(0, self.marked_vertex.shape[0] - 1)]
                self.marked_vertex = np.delete(self.marked_vertex, search_for_ellement(self.marked_vertex, new_pathed_vertex), 0)
                self.pathed_vertex = np.vstack((self.pathed_vertex, new_pathed_vertex))
                mark_vertex(new_pathed_vertex)
            else:
                new_pathed_vertex = self.marked_vertex
                self.marked_vertex = np.vstack((self.marked_vertex, self.marked_vertex + [0, 1]))
                # print("ddadada", np.delete(self.marked_vertex, search_for_ellement(self.marked_vertex, new_pathed_vertex), 0))
                self.pathed_vertex = np.vstack((self.pathed_vertex, new_pathed_vertex))
                # print("how are", new_pathed_vertex)
                mark_vertex(np.reshape(new_pathed_vertex, 2))
                self.marked_vertex = np.delete(self.marked_vertex, search_for_ellement(self.marked_vertex, new_pathed_vertex), 0)

    def convert_positions(self, array):
        adjusted_array = np.array([-2, -2])
        for x in self.array:
            adjusted_array = np.vstack(adjusted_array, [(-1) + (x[0] / (self.grid[1] / 2))])
        adjusted_array = np.delete(adjusted_array, [-2, -2])
        return adjusted_array

    def Walls(self):
        walls = gloo.Program(self.vertex1, self.fragment, count=self.marked_vertex.shape[0])
        walls["position"] = self.marked_vertex
        return walls

    def Food(self):
        food = gloo.Program(self.vertex2, self.fragment, count=self.food_vertex.shape[0])
        food["position"] = self.food_vertex
        return food
