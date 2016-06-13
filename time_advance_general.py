import matplotlib.pyplot as pyplot
import numpy as np


def time_advance_profile_with_constant_dt(advancing_func, array_init, dx, dt, n_step_max, *args):
    the_profile = [array_init]
    the_solution = array_init.copy()
    for i_step in range(1, n_step_max + 1):
        the_solution = advancing_func(the_solution, dx, dt, *args)
        the_profile.append(the_solution)
    return the_profile


def plot_profile(profile, dx, t_list, filename, title, cmin=-1.0, cmax=1.0):
    nx = len(profile[0])
    x = np.linspace(0, (nx + 1) * dx, nx + 1)
    pyplot.pcolor(x, t_list, profile)
    pyplot.clim(cmin, cmax)
    pyplot.set_cmap('PRGn')
    pyplot.title(title)
    pyplot.colorbar()
    pyplot.savefig(filename)


def plot_profile_constant_dt(profile, dx, dt, filename, title, cmin=-1.0, cmax=1.0):
    nt = len(profile)
    t_list = np.linspace(0, (nt + 1) * dt, nt + 1)
    plot_profile(profile, dx, t_list, filename, title, cmin, cmax)


def test_plot_profile():
    plot_profile([[.1, .2, -.3, .2], [-.2, .1, .4, -.2], [-.3, -.2, .1, -.2]], 1, [0, 1, 2], 'miao.png', 'Test only. ')


# test_plot_profile()
