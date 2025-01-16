from sympy import symbols, nsolve, solveset, S

def solver(expression_1, expression_2):
    x = symbols('x')

    solutions = solveset(expression_1 - expression_2, x, domain=S.Reals)

    if solutions.__class__.__name__ == "FiniteSet":
        return list(solutions)
    
    elif solutions.__class__.__name__ == "ConditionSet":

        solutions = []
        for guess in range(-100, 100, 20):
            try:
                solution = nsolve(expression_1 - expression_2, x, guess)
            except Exception:
                pass
            if solution.is_real and solution not in solutions:
                solutions.append(solution)

        return solutions
