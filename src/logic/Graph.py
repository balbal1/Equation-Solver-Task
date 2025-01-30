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

    x1_values = []
    y1_values = []
    x2_values = []
    y2_values = []
    for value in x_domain:
        if function_1.get_domain().contains(value):
            x1_values.append(value)
            y1_values.append(Float(function_1.lambda_function(value)).evalf())
        if function_2.get_domain().contains(value):
            x2_values.append(value)
            y2_values.append(Float(function_2.lambda_function(value)).evalf())
    plt.plot(x1_values, y1_values, label='f(x)')
    plt.plot(x2_values, y2_values, label='g(x)')

    same_function = False
    if len(solutions) == 0:
        same_function = True
        for i in range(len(y1_values)):
            if not allclose(float(y1_values[i]), float(y2_values[i])):
                same_function = False
                break
    else:
        for index, value in enumerate(solutions):
            y_value = Float(function_1.lambda_function(value)).evalf()
            alignment = "top" if y_value >= 0 else "bottom"
            plt.text(value, 0, "p" + str(index+1), fontsize=12, ha='center', va=alignment)
            plt.plot([value, value], [0, y_value], color='red')
            plt.scatter(value, y_value, color='red', s=50, zorder=5)

    plt.legend()
    return [fig, same_function]

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