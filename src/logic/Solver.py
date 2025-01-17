from sympy import symbols, solve, nsolve, solveset, S, re, im

def solver(expression_1, expression_2):
    x = symbols('x')


    try:
        solutions = solve(expression_1 - expression_2, x)
    
        solutions_filtered = []
        for solution in solutions:
            solution_eval = solution.evalf()
            if abs(im(solution_eval)) < 1e-10:
                solutions_filtered.append(re(solution_eval))

        return solutions_filtered
    except Exception:
        solutions = []
        for guess in range(-100, 100, 10):
            try:
                solution = nsolve(expression_1 - expression_2, x, guess)
                if solution.is_real and solution not in solutions:
                    solutions.append(solution)
            except Exception:
                pass

        return solutions        

    # if solutions.__class__.__name__ == "FiniteSet":
    #     return list(solutions)
    
    # elif solutions.__class__.__name__ == "list":
    #     return solutions
    
    # elif solutions.__class__.__name__ == "Intersection":
    #     solutions = solve(expression_1 - expression_2, x)
    #     for index, solution in enumerate(solutions):
    #         solutions[index] = re(solution.evalf())
    #     return solutions

    # elif solutions.__class__.__name__ == "ConditionSet" or not solutions:

    #     solutions = []
    #     for guess in range(-10, 10, 1):
    #         try:
    #             solution = nsolve(expression_1 - expression_2, x, guess)
    #             if solution.is_real and solution not in solutions:
    #                 solutions.append(solution)
    #         except Exception:
    #             pass

    #     return solutions
