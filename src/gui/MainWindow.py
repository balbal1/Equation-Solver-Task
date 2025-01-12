from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QTimer
from logic.Solver import solver
from sympy import sympify, latex
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from sympy import symbols
from numpy import linspace
from sympy import lambdify

functions = [{
    "expression": None,
    "symbol": "f",
    "text": None,
    "container": None,
    "input": None,
    "timer": QTimer()
}, {
    "expression": None,
    "symbol": "g",
    "text": None,
    "container": None,
    "input": None,
    "timer": QTimer()
}]

def MainWindow():

    loader = QUiLoader()
    window = loader.load("src/gui/mainwindow.ui", None)

    window.solve_button.clicked.connect(lambda: solve_handler(window))
    
    functions[0]["container"] = window.Input1Container
    functions[1]["container"] = window.Input2Container
    functions[0]["input"] = window.input1
    functions[1]["input"] = window.input2

    functions[0]["timer"].setSingleShot(True)
    functions[1]["timer"].setSingleShot(True)
    functions[0]["timer"].timeout.connect(lambda: draw_equation(functions[0]))
    functions[1]["timer"].timeout.connect(lambda: draw_equation(functions[1]))

    functions[0]["input"].textChanged.connect(lambda: input_change_handler(functions[0]))
    functions[1]["input"].textChanged.connect(lambda: input_change_handler(functions[1]))
    input_change_handler(functions[0])
    input_change_handler(functions[1])

    return window

def draw_equation(function):
    fig, ax = plt.subplots()
    ax.text(0.5, 0.5, function["text"], fontsize=20, ha='center', va='center')
    ax.axis('off')
    graph = FigureCanvasQTAgg(fig)
    graph.setMaximumHeight(100)
    function["container"].itemAt(2).widget().setParent(None)
    function["container"].addWidget(graph)
    plt.close(fig)

def input_change_handler(function):
    text = function["input"].text()
    if text == "":
        function["text"] = f'{function["symbol"]}(x) = '
        function["timer"].start(100)
        return
    
    try:
        function["expression"] = sympify(text)
        function["text"] = rf'${function["symbol"]}(x) = {latex(function["expression"])}$'
    except Exception:
        function["text"] = "Invalid input!"
    
    function["timer"].start(100)


def solve_handler(window):
    equation_1 = window.input1.text()
    equation_2 = window.input2.text()

    solutions = solver(equation_1, equation_2)

    for index in range(window.solutions_table.rowCount(), -1, -1):
        window.solutions_table.removeRow(index)

    for index, solution in enumerate(solutions):
        window.solutions_table.insertRow(index)
        window.solutions_table.setItem(index, 0, QTableWidgetItem(str(solution)))

    x = symbols('x')
    x_vals = linspace(-10, 10, 100)

    fig = plt.figure()

    lam_x = lambdify(x, functions[0]["expression"], modules=['numpy'])
    y_vals = lam_x(x_vals)

    plt.plot(x_vals, y_vals)

    lam_x = lambdify(x, functions[1]["expression"], modules=['numpy'])
    y_vals = lam_x(x_vals)

    plt.plot(x_vals, y_vals)

    graph = FigureCanvasQTAgg(fig)
    window.SolutionContainer.itemAt(1).widget().setParent(None)
    window.SolutionContainer.addWidget(graph)
    plt.close(fig)

