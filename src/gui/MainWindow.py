from PySide2.QtUiTools import QUiLoader
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from logic.Function import Function
from logic.SolverThread import SolverThread
from gui.SolveButton import SolveButton
from gui.SolutionsTable import SolutionsTable

def init_program():
    """
    Loads the UI file and initialize main window.

    Returns:
        MainWindow: The MainWindow of the program.
    """
    
    loader = QUiLoader()
    window = loader.load("src/gui/mainwindow.ui", None)
    return MainWindow(window)

class MainWindow:

    def __init__(self, window):

        self.window = window
        self.loading = False
        self.solve_thread = None

        self.table = SolutionsTable(self.window.solution_table)

        self.button = SolveButton(self.window.solve_button)
        self.button.body.clicked.connect(self.solve_handler)

        self.function_1 = Function("f", self.window.input1, self.window.input1_function)
        self.function_2 = Function("g", self.window.input2, self.window.input2_function)

        self.function_1.disable.connect(self.button.disable)
        self.function_2.disable.connect(self.button.disable)

    def solve_handler(self):
        """
        Handles the solve button click event.
        """

        if self.loading:
            return

        if self.function_1.error or self.function_2.error:
            return

        self.loading = True
        self.button.set_loading()

        self.solve_thread = SolverThread(self)
        self.solve_thread.finished.connect(self.show_solution)
        self.solve_thread.start()

    def show_solution(self, solutions, figure, flag):
        """
        Show the solution after solution thread finishes.
        
        Args:
            solutions (list): The list of solution values to display.
            figure (object): The matplotlib figure object.
            flag: Boolean that is true if the two functions are the same.
        """

        self.table.show_solution(solutions, flag)

        graph = FigureCanvasQTAgg(figure)
        self.window.solution_graph.itemAt(0).widget().setParent(None)
        self.window.solution_graph.addWidget(graph)
        plt.close(figure)

        self.loading = False
        self.button.set_finished()    
        self.solve_thread = None
