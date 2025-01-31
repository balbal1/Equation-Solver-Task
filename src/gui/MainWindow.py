from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QThread, Signal, Qt
from logic.Solver import solver
from logic.Graph import draw_graph
from logic.Function import Function
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

def init_program():
    loader = QUiLoader()
    window = loader.load("src/gui/mainwindow.ui", None)
    return MainWindow(window)

class SolverThread(QThread):
    finished = Signal(object, object, bool)

    def __init__(self, parent_window):
        super().__init__()
        self.parent_window = parent_window

    def run(self):
        solutions = solver(self.parent_window.function_1.expression, self.parent_window.function_2.expression)
        figure, flag = draw_graph(self.parent_window.function_1, self.parent_window.function_2, solutions)
        self.finished.emit(solutions, figure, flag)

class MainWindow:

    def __init__(self, window):

        self.window = window
        self.loading = False
        self.solve_thread = None

        self.window.solution_table.setColumnWidth(0, 100)
        self.window.solution_table.setColumnWidth(1, 248)

        self.function_1 = Function("f", self.window.input1, self.window.input1_function)
        self.function_2 = Function("g", self.window.input2, self.window.input2_function)

        self.window.solve_button.clicked.connect(self.solve_handler)

    def solve_handler(self):

        if self.loading:
            return

        if self.function_1.error or self.function_2.error:
            return

        self.loading = True
        self.window.solve_button.setText("Processing...")
        self.window.solve_button.setProperty("isLoading", "true")
        self.render_solve_button()

        self.solve_thread = SolverThread(self)
        self.solve_thread.finished.connect(self.show_solution)
        self.solve_thread.start()

    def show_solution(self, solutions, figure, same_function):

        for index in range(self.window.solution_table.rowCount(), -1, -1):
            self.window.solution_table.removeRow(index)

        if len(solutions) == 0:
            self.window.solution_table.setColumnWidth(0, 0)
            self.window.solution_table.setColumnWidth(1, 348)
            self.window.solution_table.insertRow(index)
            if same_function:
                message = "The solutions are infinite"
            else:
                message = "No solution exists"
            item = QTableWidgetItem(message)
            item.setTextAlignment(Qt.AlignCenter)
            self.window.solution_table.setItem(index, 1, item)
                
        else:
            self.window.solution_table.setColumnWidth(0, 100)
            self.window.solution_table.setColumnWidth(1, 248)
            for index, solution in enumerate(solutions):
                self.window.solution_table.insertRow(index)
                item = QTableWidgetItem("p" + str(index+1))
                item.setTextAlignment(Qt.AlignCenter)
                self.window.solution_table.setItem(index, 0, item)
                item = QTableWidgetItem(str(solution))
                item.setTextAlignment(Qt.AlignCenter)
                self.window.solution_table.setItem(index, 1, item)

        graph = FigureCanvasQTAgg(figure)
        self.window.solution_graph.itemAt(0).widget().setParent(None)
        self.window.solution_graph.addWidget(graph)
        plt.close(figure)

        self.loading = False
        self.window.solve_button.setText("Solve")
        self.window.solve_button.setProperty("isLoading", "false")
        self.render_solve_button()
    
        self.solve_thread = None

    def render_solve_button(self):
        self.window.solve_button.style().unpolish(self.window.solve_button)
        self.window.solve_button.style().polish(self.window.solve_button)
        self.window.solve_button.update()
