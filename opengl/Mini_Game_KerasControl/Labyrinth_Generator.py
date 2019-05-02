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

    else:
        # transform into mx+b function
        m = target[0] / target[1]

        def tempvar():
            # intiger of the x value
            t = math.floor(target[1])
            return t

        y = np.zeros([tempvar(), 10])
        count = 0

        for x in range(tempvar()):
            for n in range(10):
                y[x, n] = m * ((x * 10 + n) / 10)

        for x in range(y.shape[0]):
            for n in range(math.floor(target[0])):
                print(n)
                condition = False
                for i in range(y.shape[1]):
                    if not condition and y[x, i] < n + 1 and y[x, i] > n:
                        condition = True
                        count += 1
        return(count)


def check_path_perimiter(point_list):
    pass


def generate_goals(amount=1):

    for x in range(amount):
        goals = np.append(goals, [math.floor(10 * random.random()), math.floor(10 * random.random())])


def generate_path_to_goal(goal, length, amount):
    pass


def generate_path_avoiding_goal():
    pass


def generate_point_matrix():
    pass


def generate_labyrinth():
    pass


print(check_shortest_distance(np.array([2, 3])))
