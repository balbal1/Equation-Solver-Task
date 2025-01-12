from sympy import sympify, symbols, solveset, S

def solver(expression_1, expression_2):
    x = symbols('x')
    
    function_1 = sympify(expression_1)
    function_2 = sympify(expression_2)

    solutions = solveset(function_1 - function_2, x, domain=S.Reals)
    
    return solutions