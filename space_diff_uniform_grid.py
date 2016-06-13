# the boundary unable to compute the value shall be zero.
import numpy as np


def forward_array(array_val):
    array_advanced_val = np.zeros(len(array_val))
    for i in range(0, len(array_val) - 1):
        array_advanced_val[i] = array_val[i + 1]
    array_advanced_val[len(array_val) - 1] = array_val[len(array_val) - 1]
    return array_advanced_val


def backward_array(array_val):
    array_backward_val = np.zeros(len(array_val))
    for i in range(1, len(array_val)):
        array_backward_val[i] = array_val[i - 1]
    array_backward_val[0] = array_val[0]
    return array_backward_val


def forward_diff_1d(array_val, dx):
    array_advanced_val = forward_array(array_val)
    return (array_advanced_val - array_val) / dx


def backward_diff_1d(array_val, dx):
    array_backward_val = backward_array(array_val)
    return (array_val - array_backward_val) / dx


def central_diff_1d(array_val, dx):
    array_advanced_val = forward_array(array_val)
    array_backward_val = backward_array(array_val)
    return (array_advanced_val - array_backward_val) / (2 * dx)


