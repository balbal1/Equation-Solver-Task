import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PySide2.QtCore import Qt
from gui.MainWindow import init_program
import pytest

@pytest.mark.parametrize("fx, gx, expected_solutions", [
    ("x", "2*x", [0]),
    ("3*x - 1", "-7*x + 5", [0.6]),
    ("x^2 + 2*x", "-x + 10", [-5, 2]),
    ("4*x^2 - 3*x", "x^3/(x-4) + 5", [-0.81615, 1.42756, 5.72192]),
    ("4*x^4 + x^3 - 258*x^2+ 50*x + 1500", "-2*x^4 + x^3 - 58*x - 660", [-6, -3, 4, 5]),
    ("log(x-5)", "0.2*x^2 - 10*x + 100", [13.35465, 36.9297]),
    ("sqrt(3*x + 7) - 0.2*x", "(x-8)/(4*x)", [-2.14372, -1.03637, 75.0806])
])
def test_main_program(qtbot, fx, gx, expected_solutions):
    program = init_program()
    qtbot.addWidget(program.window)

    qtbot.keyClicks(program.window.input1, fx)
    qtbot.keyClicks(program.window.input2, gx)
    qtbot.mouseClick(program.window.solve_button, Qt.MouseButton.LeftButton)

    qtbot.waitUntil(lambda: program.window.solution_table.rowCount() != 0, timeout=20000)

    assert program.window.solution_table.rowCount() == len(expected_solutions)
    assert len(program.graph_axes.lines) == len(expected_solutions) + 2

    for index in range(program.window.solution_table.rowCount()):
        assert float(program.window.solution_table.item(index, 1).text()) in expected_solutions
