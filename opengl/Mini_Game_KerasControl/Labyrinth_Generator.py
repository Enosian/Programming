import numpy as np
import random

random.seed(420)
a = np.empty([1])
goal_paths = []
avoidance_paths = []


def check_shortest_distance(goal, origin):
    pass


def check_path_perimiter(point_list):
    pass


def generate_goals(amount=1):
    for x in range(amount):
        goal = np.append(goal, [int(10 * random.random()), int(10 * random.random())])


def generate_path_to_goal(goal, length, amount):
    pass


def generate_path_avoiding_goal():
    pass


def generate_point_matrix():
    pass


def generate_labyrinth():
    pass
