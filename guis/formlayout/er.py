import numpy as np
import random


x = np.array([6, 6])
y = np.array([1, 0])


def mark_vertex(vertex):
    global x
    x = np.vstack((x, [vertex[0], vertex[1] + 1]))
    x = np.vstack((x, [vertex[0], vertex[1] - 1]))
    x = np.vstack((x, [vertex[0] + 1, vertex[1]]))
    x = np.vstack((x, [vertex[0] - 1, vertex[1]]))
    x = np.delete(x, 0, axis=0)


def filter_vertex():
    global x
    to_delete = np.array([])
    for l in range(x.shape[0]):
        if len(y.shape) > 1:
            for n in y:
                if x[l, 0] == n[0] and x[l, 1] == n[1]:
                    print("on path: {0} {1}".format(x[l], n))
                    to_delete = np.append(to_delete, l)
                    print(to_delete)
        else:
            if x[l, 0] == y[0] and x[l, 1] == y[1]:
                print("on path: {0} {1}".format(x[l], y))
                to_delete = np.append(to_delete, l)
        for m in range(1 + l, x.shape[0] - 1):

            if x[l, 0] == x[m, 0] and x[l, 1] == x[m, 1]:
                print("same: {0} {1} future conditions: index 0({2}) index(0){3} current y position 1 = {4} current y position 2 ={5} ".format(x[l], x[m], x[l, 0] == x[m, 0], x[l, 1] == x[m, 1], l, m))
                to_delete = np.append(to_delete, m)
            elif np.linalg.norm(x[l] - x[m]) < 1.4:
                print("distance:{0} {1} future conditions: index 0({2}) index(0){3} current y position 1 = {4} current y position 2 ={5} ".format(x[l], x[m], x[l] - x[m], np.linalg.norm(x[l] - x[m]), l, m))
                to_delete = np.append(to_delete, m)

    for o in to_delete:
        x = np.delete(x, o, axis=0)


def search_for_ellement(array, ellement):
    # print("array:", array, "ellement:", ellement)
    for k in range(array.shape[0]):
        # print("hallo", array[x])
        if ellement[0] == array[k, 0] and ellement[1] == array[k, 1]:
            print(k)
            return k
            break
        else:
            raise Exception('ellement {0} was not found in array {1}'.format(ellement, array))


if __name__ == '__main__':

    mark_vertex(y)
    filter_vertex()
    print(x)
    for p in range(10):
        print(x)
        new_path = np.array(x[random.randint(0, x.shape[0] - 1)])
        mark_vertex(new_path)
        filter_vertex()
    print(x)
