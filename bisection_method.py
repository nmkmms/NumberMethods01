"""https://en.wikipedia.org/wiki/Bisection_method"""
from math import *


def bisection_method(func, a, b, epsilon, depth=1):
    if abs(func(a)) < epsilon:
        return a, depth
    if abs(func(b)) < epsilon:
        return b, depth
    assert func(a) < 0 < func(b) or func(b) < 0 < func(a), \
        f'func({a}) = {func(a)} func({b}) = {func(b)}'

    c = (a + b) / 2

    if func(a) < 0 < func(b):
        if func(c) < 0:
            return bisection_method(func, c, b, epsilon, depth+1)
        return bisection_method(func, a, c, epsilon, depth+1)
    if func(c) < 0:
        return bisection_method(func, a, c, epsilon, depth+1)
    return bisection_method(func, c, b, epsilon, depth+1)


if __name__ == '__main__':
    result, depth = bisection_method(lambda x: x ** 2 - x - 6, 0, 10, 1e-16)
    print(f'Result for x^2 - x - 6 on [0, 10]: x = {result}\n# of steps: {depth}')

    result, depth = bisection_method(lambda x: cos(x) - 0.3 * sin(x), pi/4, pi/2, 1e-12)
    print(f'Result for cos(x) - 0.3 * sin(x) on [π/4, π/2]: x = {result}\n# of steps: {depth}')

    result, depth = bisection_method(lambda x: x-sin(x)-0.5, 0, 5, 1e-12)
    print(f'Result for x - sin(x) - 0.5 on [0, 5]: x = {result}\n# of steps: {depth}')
