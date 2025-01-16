from sympy import symbols
from numpy import linspace, array
from sympy import lambdify
import matplotlib.pyplot as plt

def draw_graph(function_1, function_2, solutions):
    x = symbols('x')

    domain = center_graph(solutions)

    fig, ax = plt.subplots()

    # ax.set_aspect('equal')
    ax.grid(True, which='both')

    # set the x-spine (see below for more info on `set_position`)
    ax.spines['left'].set_position('zero')
    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')
    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    x_domain = linspace(domain[0], domain[1], 100)

    lam_x = lambdify(x, function_1.expression, modules=['sympy'])
    x_values = []
    y_values = []
    for value in x_domain:
        if function_1.get_domain().contains(value):
            x_values.append(value)
            y_values.append(lam_x(value).evalf())
    plt.plot(x_values, y_values, label='f(x)')

    lam_x = lambdify(x, function_2.expression, modules=['sympy'])
    x_values = []
    y_values = []
    for value in x_domain:
        if function_2.get_domain().contains(value):
            x_values.append(value)
            y_values.append(lam_x(value).evalf())
    plt.plot(x_values, y_values, label='g(x)')

    y_values = []
    for value in solutions:
        y_values.append(lam_x(value).evalf())
    plt.scatter(list(solutions), y_values, color='red', label='solutions', s=100, zorder=5)
    
    plt.legend()
    return fig

def center_graph(solutions):
    minimum = min(0, min(solutions))
    maximum = max(0, max(solutions))
    
    diff = maximum - minimum
    minimum -= diff * 0.2
    maximum += diff * 0.2
    
    return [minimum, maximum]