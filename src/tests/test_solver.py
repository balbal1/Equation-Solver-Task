import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from logic.Solver import solver
from sympy import sympify
import pytest

@pytest.mark.parametrize("fx, gx, expected_solutions", [
    ("x",                       "2*x",                  [0]                             ),
    ("3*x - 1",                 "-7*x + 5",             [0.6]                           ),
    ("x^2 + 2*x",               "-x + 10",              [-5, 2]                         ),
    ("4*x^2 - 3*x",             "x^3/(x-4) + 5",        [-0.81615, 1.42756, 5.72192]    ),
    ("sqrt(3*x + 7) - 0.2*x",   "(x-8)/(4*x)",          [-2.14372, -1.03637, 75.0806]   ),
    ("log(x-5)",                "0.2*x^2 - 10*x + 100", [13.35465, 36.9297]             )
])
def test_solver(fx, gx, expected_solutions):
    expression_1 = sympify(fx)
    expression_2 = sympify(gx)

    solutions = solver(expression_1, expression_2)
    assert len(solutions) == len(expected_solutions)

    for solution in solutions:
        assert solution in expected_solutions

