import initializer as init
import time_advance_general as advance
import constant_advancing_eq as eq
import numpy as np


def show_instable_scheme():
    npoints = 128
    dx = 0.1
    dt = 0.1
    a = 1
    nstep = 128
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.central_space_central_time, init_case, dx, dt, nstep, a)
    advance.plot_profile_constant_dt(profile, dx, dt, 'miao.png', 'Instable Scheme', cmax = 5.0, cmin = -5.0)


show_instable_scheme()
