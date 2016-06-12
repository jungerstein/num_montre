import matplotlib.pyplot as pyplot
import numpy as np


def time_advance_profile_with_constant_dt(advancing_func, array_init, dx, dt, n_step_max, *args):
    the_profile = [array_init]
    the_solution = array_init.copy()
    for i_step in range(1, n_step_max + 1):
        the_solution = advancing_func(the_solution, dx, dt, *args)
        the_profile.append(the_solution, dx, dt)
    return the_profile


def plot_profile(profile, dx, dt_list, filename, title, cmin=-1.0, cmax=1.0):
    nx = len(profile[0])
    x = np.linspace(0, (nx + 1) * dx, nx + 1)
    pyplot.pcolorfast(x, dt_list, profile)
    pyplot.clim(cmin, cmax)
    pyplot.set_cmap('PrGn')
    pyplot.title(title)
    pyplot.colorbar()
    pyplot.savefig(filename)
