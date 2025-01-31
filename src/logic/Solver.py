from sympy import symbols, solve, nsolve, re, im

def solver(expression_1, expression_2):
    """
    Solves the two given expressions together.

    Args:
        expression_1 (object): First input function.
        expression_2 (object): Second input function.
    
    Returns:
        list: List of all solutions to the two expressions.
    """

    x = symbols('x')

    try:
        unfiltered_solutions = solve(expression_1 - expression_2, x)
    
        solutions = []
        for solution in unfiltered_solutions:
            solution_eval = solution.evalf()
            if abs(im(solution_eval)) < 1e-10:
                solutions.append(re(solution_eval))

    except Exception:

        solutions = []        
        for guess in range(-100, 100, 10):
            try:
                solution = nsolve(expression_1 - expression_2, x, guess)
                if solution.is_real and solution not in solutions:
                    solutions.append(solution)
            except Exception:
                pass

    rounded_solutions = []
    for solution in solutions:
        rounded_solutions.append(round(float(solution), 5))

    return rounded_solutions
