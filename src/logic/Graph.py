from numpy import linspace, allclose
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

    domain = center_graph(solutions, function_1, function_2)
    x_domain = linspace(domain[0], domain[1], 100)

    max_y = 6
    min_y = -6
    
    same_function = False
    if len(solutions) == 0:
        same_function = True
    else:
        for index, value in enumerate(solutions):
            y_value = Float(function_1.lambda_function(value)).evalf()
            min_y = min(min_y, y_value)
            max_y = max(max_y, y_value)
            alignment = "top" if y_value >= 0 else "bottom"
            plt.text(value, 0, "p" + str(index+1), fontsize=12, ha='center', va=alignment)
            plt.plot([value, value], [0, y_value], color='red')
            plt.scatter(value, y_value, color='red', s=50, zorder=5)

    min_y *= 2.5
    max_y *= 2.5

    y1_values = function_1.evaluate_function(x_domain, min_y, max_y)
    plt.plot(x_domain, y1_values, label='f(x)')
    
    y2_values = function_2.evaluate_function(x_domain, min_y, max_y)
    plt.plot(x_domain, y2_values, label='g(x)')

    if same_function:
        for i in range(len(y1_values)):
            if y1_values[i] == y1_values[i] and y2_values[i] == y2_values[i]:
                if not allclose(float(y1_values[i]), float(y2_values[i])):
                    same_function = False
                    break

    plt.legend()
    return fig, same_function

def center_graph(solutions, function_1, function_2):
    if solutions == []:
        domain_endpoints = []
        domain_endpoints.extend(list(function_1.get_domain().boundary))
        domain_endpoints.extend(list(function_2.get_domain().boundary))
        
        if len(domain_endpoints) == 0:
            return [Float(-15), Float(15)]
        else:
            minimum = min(domain_endpoints[0], domain_endpoints[0])
            maximum = max(domain_endpoints[-1], domain_endpoints[-1])

    else:    
        minimum = min(0, min(solutions))
        maximum = max(0, max(solutions))
    
    diff = max(maximum - minimum, 30)
    minimum -= diff * 0.2
    maximum += diff * 0.2
    
    return [minimum, maximum]