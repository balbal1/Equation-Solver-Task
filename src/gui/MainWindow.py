from PySide2.QtWidgets import QTableWidgetItem, QFrame
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

        self.window.solution_table.setColumnWidth(0, 100)
        self.window.solution_table.setColumnWidth(1, 248)

        self.function_1 = Function("f", self.window.input1, self.window.input1_function)
        self.function_2 = Function("g", self.window.input2, self.window.input2_function)

        self.window.solve_button.clicked.connect(self.solve_handler)

    def solve_handler(self):

        solutions = solver(self.function_1.expression, self.function_2.expression)

        figure = draw_graph(self.function_1, self.function_2, solutions)

        for index in range(self.window.solution_table.rowCount(), -1, -1):
            self.window.solution_table.removeRow(index)

        for index, solution in enumerate(solutions):
            self.window.solution_table.insertRow(index)
            self.window.solution_table.setItem(index, 0, QTableWidgetItem("p" + str(index+1)))
            self.window.solution_table.setItem(index, 1, QTableWidgetItem(str(solution)))

        graph = FigureCanvasQTAgg(figure)
        self.window.solution_graph.itemAt(0).widget().setParent(None)
        self.window.solution_graph.addWidget(graph)
        plt.close(figure)

