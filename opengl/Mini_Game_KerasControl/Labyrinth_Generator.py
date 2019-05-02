import numpy as np
import random
import math

random.seed(420)
goals = np.empty([1])
goal_paths = []
avoidance_paths = []


def check_shortest_distance(p_target, p_origin=np.zeros([2])):
    m = 0
    target = p_target - p_origin

    if target[0] == 0:
        return abs(target[1])

    elif target[1] == 0:
        return abs(target[0])

    elif target[0] / target[1] > 1:
        m = target[1] / target[0]
        return target[1] * math.ceil(m)

    elif target[0] / target[1] <= 1:
        m = target[0] / target[1]
        return target[1] * math.ceil(m)


def check_path_perimiter(point_list):
    pass


def generate_goals(amount=1):

    for x in range(amount):
        goals = np.append(goals, [int(10 * random.random()), int(10 * random.random())])


def generate_path_to_goal(goal, length, amount):
    pass


def generate_path_avoiding_goal():
    pass


def generate_point_matrix():
    pass


def generate_labyrinth():
    pass
