import space_diff_uniform_grid as spacediff


# Solve u_{, t} + a u_{, x} = 0.
def constant_advancing_euler_eq(old_solution, dudx_method, a, dx, dt):
    dudx = dudx_method(old_solution, dx)
    dudt = (-a) * dudx
    # TODO do not forget to refactor boundary condition out.
    dudt[0] = dudt[1]
    dudt[-1] = dudt[-2]
    return old_solution + dudt * dt


def forward_space_forward_time(old_solution, dx, dt, a):
    return constant_advancing_euler_eq(old_solution, spacediff.forward_diff_1d, a, dx, dt)


def central_space_forward_time(old_solution, dx, dt, a):
    return constant_advancing_euler_eq(old_solution, spacediff.central_diff_1d, a, dx, dt)


def backward_space_forward_time(old_solution, dx, dt, a):
    return constant_advancing_euler_eq(old_solution, spacediff.backward_diff_1d, a, dx, dt)

