import numpy as np
import random

random.seed(100)


x = np.array([int(10 * random.random()), int(10 * random.random()), int(10 * random.random()), int(10 * random.random()), int(10 * random.random()), int(10 * random.random()), int(10 * random.random()), int(10 * random.random())])
count = 0


# def pair():
#     global count
#     matches = []
#     for i in range(len(x) - 1):
#         for k in range(len(x) - i):
#             if x[i] + x[k + i] == 10:
#                 count += 1
#             elif x[i] + x[k + i] < 10:
#                 matches.append(x[i] + x[k + i])
#     return matches


def match(array_1, array_2):
    global count
    matches = []
    for i in range(len(array_1)):
        for k in range(len(array_2)):
            if array_1[i] + array_2[k] == 10:
                count += 1
                print(array_1[i], array_2[k])
            elif array_1[i] + array_2[k] < 10:
                matches.append(array_1[i] + array_2[k])
    return matches


k = match(x, x)
print(k)
k = match(k, x)
print(k)
k = match(k, x)
print(k)
k = match(k, x)
print(count, x)
