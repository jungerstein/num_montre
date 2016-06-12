def time_advance_profile_with_constant_dt(advancing_func, array_init, dx, dt, n_step_max, *args):
    the_profile = [array_init]
    the_solution = array_init.copy()
    for i_step in range(1, n_step_max + 1):
        the_solution = advancing_func(the_solution, dx, dt, *args)
        the_profile.append(the_solution, dx, dt)
    return the_profile
