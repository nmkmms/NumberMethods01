"""https://en.wikipedia.org/wiki/Fixed-point_iteration"""
from math import *


def simple_iteration_method(func, x_approx, epsilon):
    x = func(x_approx)
    steps = 1
    while abs(x - x_approx) > epsilon:
        steps += 1
        x_approx = x
        x = func(x_approx)
    return x, steps


if __name__ == '__main__':
    result, steps = simple_iteration_method(lambda x: (exp(x)+x**3 + 4*x**2 + 2*x + 2)/(x**2 + 3*x - 3), -2, 1e-10)
    print(f'Result for f(x) = exp[-x] * (x^2+5x+2) + 1: x = {result}\n# of steps: {steps}')

    result, steps = simple_iteration_method(lambda x: sin(x) + 1/2, 2, 1e-10)
    print(f'Result for f(x) = x-sin[x]-(1/2): x = {result}\n# of steps: {steps}')

    result, steps = simple_iteration_method(lambda x: exp(exp(-x)/3), 2, 1e-10)
    print(f'Result for f(x) = exp[-x] = 3log[x]: x = {result}\n# of steps: {steps}')

    result, steps = simple_iteration_method(lambda x: log(sin(2 * x)) + 1, 1, 1e-10)
    print(f'Result for f(x) = sin[2x]-exp[x-1]: x = {result}\n# of steps: {steps}')
