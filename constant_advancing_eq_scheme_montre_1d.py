import initializer as init
import time_advance_general as advance
import constant_advancing_eq as eq
import numpy as np


def show_instable_scheme():
    npoints = 200
    dx = 0.05
    dt = 0.06
    a = 1
    nstep = 60
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.central_space_forward_time, init_case, dx, dt, nstep, a)
    profile_taken_out = [profile_at_a_timepoint[45:140] for profile_at_a_timepoint in profile]
    advance.plot_profile_constant_dt(profile_taken_out, dx, dt, 'output/instable_scheme.png',
                                     'Instable Scheme, dx = ' + str(dx) + ', dt = ' + str(dt) + ', a = ' + str(a),
                                     cmax = 1.5, cmin = -1.5)


def show_backward_scheme_large_CFL():
    npoints = 200
    dx = 0.05
    dt = 0.075
    a = 1
    nstep = 40
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.backward_space_forward_time, init_case, dx, dt, nstep, a)
    profile_taken_out = [profile_at_a_timepoint[45:140] for profile_at_a_timepoint in profile]
    advance.plot_profile_constant_dt(profile_taken_out, dx, dt, 'output/large_CFL.png',
                                     'Upwind, dx = ' + str(dx) + ', dt = ' + str(dt) + ', a = ' + str(a),
                                     cmax = 1.5, cmin = -1.5)


def show_backward_scheme_small_CFL():
    npoints = 200
    dx = 0.05
    dt = 0.03
    a = 1
    nstep = 100
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.backward_space_forward_time, init_case, dx, dt, nstep, a)
    profile_taken_out = [profile_at_a_timepoint[45:140] for profile_at_a_timepoint in profile]
    advance.plot_profile_constant_dt(profile_taken_out, dx, dt, 'output/small_CFL.png',
                                     'Upwind, dx = ' + str(dx) + ', dt = ' + str(dt) + ', a = ' + str(a),
                                     cmax = 1.5, cmin = -1.5)


def show_forward_scheme_small_CFL():
    npoints = 200
    dx = 0.05
    dt = 0.03
    a = 1
    nstep = 100
    init_case = np.array(init.sin_x_1p7(npoints, dx))
    profile = advance.time_advance_profile_with_constant_dt(eq.forward_space_forward_time, init_case, dx, dt, nstep, a)
    profile_taken_out = [profile_at_a_timepoint[45:140] for profile_at_a_timepoint in profile]
    advance.plot_profile_constant_dt(profile_taken_out, dx, dt, 'output/wrong_direction.png',
                                     'Downwind, dx = ' + str(dx) + ', dt = ' + str(dt) + ', a = ' + str(a),
                                     cmax = 1.5, cmin = -1.5)


show_instable_scheme()
show_backward_scheme_large_CFL()
show_backward_scheme_small_CFL()
show_forward_scheme_small_CFL()
