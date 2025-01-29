from sympy import symbols
from numpy import linspace
from sympy import Float
import matplotlib.pyplot as plt

def draw_graph(function_1, function_2, solutions):

    fig, ax = plt.subplots()
    ax.grid(True, which='both')

    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    domain = center_graph(solutions)
    x_domain = linspace(domain[0], domain[1], 100)

    x_values = []
    y_values = []
    for value in x_domain:
        if function_1.get_domain().contains(value):
            x_values.append(value)
            y_values.append(Float(function_1.lambda_function(value)).evalf())
    plt.plot(x_values, y_values, label='f(x)')

    x_values = []
    y_values = []
    for value in x_domain:
        if function_2.get_domain().contains(value):
            x_values.append(value)
            y_values.append(Float(function_2.lambda_function(value)).evalf())
    plt.plot(x_values, y_values, label='g(x)')

    for index, value in enumerate(solutions):
        y_value = Float(function_1.lambda_function(value)).evalf()
        alignment = "top" if y_value >= 0 else "bottom"
        plt.text(value, 0, "p" + str(index+1), fontsize=12, ha='center', va=alignment)
        plt.plot([value, value], [0, y_value], color='red')
        plt.scatter(value, y_value, color='red', s=50, zorder=5)

    plt.legend()
    return fig

def center_graph(solutions):
    if solutions == []:
        return [Float(-15), Float(15)]
    
    minimum = min(0, min(solutions))
    maximum = max(0, max(solutions))
    
    diff = max(maximum - minimum, 15)
    minimum -= diff * 0.2
    maximum += diff * 0.2
    
    return [minimum, maximum]