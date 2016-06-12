import numpy as np
# for testers
import matplotlib.pyplot as pyplot


def sin_x_1p7(n_points, dx):
    return [np.sin((i * dx)**1.7) for i in range(n_points)]


def test_initial():
    n_points = 180
    dx = 0.1
    x = np.linspace(0, (n_points - 1) * dx, num=n_points)
    y = sin_x_1p7(n_points, dx)
    pyplot.plot(x, y)
    pyplot.savefig("miao.png")
    return


#test_initial()