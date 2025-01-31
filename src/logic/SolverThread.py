from PySide2.QtCore import QThread, Signal
from logic.Solver import solver
from logic.Graph import draw_graph

class SolverThread(QThread):
    finished = Signal(object, object, bool)

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

    def run(self):
        solutions = solver(self.parent_window.function_1.expression, self.parent_window.function_2.expression)
        figure, flag = draw_graph(self.parent_window.function_1, self.parent_window.function_2, solutions)
        self.finished.emit(solutions, figure, flag)