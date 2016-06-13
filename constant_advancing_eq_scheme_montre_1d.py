import initializer as init
import time_advance_general as advance
import constant_advancing_eq as eq
import numpy as np


def show_instable_scheme():
    npoints = 95
    dx = 0.05
    dt = 0.06
    a = 1
    nstep = 20
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.central_space_central_time, init_case, dx, dt, nstep, a)
    advance.plot_profile_constant_dt(profile, dx, dt, 'output/instable_scheme.png',
                                     'Instable Scheme, dx = ' + str(dx) + ', dt = ' + str(dt),
                                     cmax = 2.0, cmin = -2.0)


show_instable_scheme()
