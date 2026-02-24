import matplotlib.pyplot as plt
import numpy as np


def logistic_equation(r, x0, n=10000):
    '''
    Compute logistic equation, return list on n values

    '''
    x_values = [x0]
    while len(x_values) < n:
        x_values.append(r*x_values[-1]*(1-x_values[-1]))
    return x_values

def logistic_tail(r, x0, n=10000, tail=200):
    '''
    Compute only the final 'tail' values of the logistic map
    instead of storing the entire trajectory.

    '''
    x = x0
    values = []

    for i in range(n):
        x = r * x * (1 - x)

        if i >= n - tail:
            values.append(x)

    return values


def distinct_points(values, tol=1e-3):
    '''
    Idenify distinct points up to tolerence level from list of values
    '''
    values = sorted(values)
    points = [values[0]]
    for v in values[1:]:
        if abs(v - points[-1]) > tol:
            points.append(v)
    return points

def find_n_cycles(r_values, n, x0=0.1, total_iter=1000, tail=100, tol=1e-3):
    '''
    Find values of r which produce an n-cycle
    '''
    results = []
    for r in r_values:
        tail_values = logistic_tail(r, x0, n=total_iter, tail=tail)
    
        if len(distinct_points(tail_values, tol=tol)) == n:
            results.append(r)

    return results


def liapunov(r, n, x0=0.1, bin=300):
    '''
    Calculate Liapunov exponent
    '''
    x = x0
    
    for _ in range(bin):
        x = r * x * (1 - x)

    total = 0
    for i in range(n):
        x = r * x * (1 - x)
        total += np.log(abs(r * (1 - 2*x) ))
    
    return total / n


if __name__ == "__main__":
     # print(distinct_points(logistic_equation(3, 0.2, n=500)[250:]))
     pass