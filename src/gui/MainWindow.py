from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from logic.Solver import solver
from logic.Graph import draw_graph
from logic.Function import Function
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

def init_program():
    loader = QUiLoader()
    window = loader.load("src/gui/mainwindow.ui", None)
    return MainWindow(window)

class MainWindow:

    def __init__(self, window):

        self.window = window

        self.function_1 = Function("f", self.window.input1, self.window.Input1Container)
        self.function_2 = Function("g", self.window.input2, self.window.Input2Container)

        self.window.solve_button.clicked.connect(self.solve_handler)

    def solve_handler(self):

        solutions = solver(self.function_1.expression, self.function_2.expression)

        figure = draw_graph(self.function_1, self.function_2, solutions)

        for index in range(self.window.solutions_table.rowCount(), -1, -1):
            self.window.solutions_table.removeRow(index)

        for index, solution in enumerate(solutions):
            self.window.solutions_table.insertRow(index)
            self.window.solutions_table.setItem(index, 0, QTableWidgetItem(str(solution)))

        graph = FigureCanvasQTAgg(figure)
        self.window.SolutionContainer.itemAt(1).widget().setParent(None)
        self.window.SolutionContainer.addWidget(graph)
        plt.close(figure)

