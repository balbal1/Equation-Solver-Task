from PySide2.QtCore import QTimer
from sympy import symbols, sympify, lambdify, latex, S
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from sympy.calculus.util import continuous_domain

class Function:

    def __init__(self, symbol, input, container):
        self.symbol = symbol
        self.text = None
        self.expression = None
        self.input = input
        self.container = container
        self.timer = QTimer()
        self.error = True

        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.draw_function)

        self.input.textChanged.connect(self.input_change_handler)
        self.input_change_handler()


    def draw_function(self):
        fig, ax = plt.subplots()
        ax.text(0, 0.5, self.text, fontsize=20, ha='left', va='center')
        ax.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        graph = FigureCanvasQTAgg(fig)
        graph.setMaximumHeight(80)
        self.container.itemAt(0).widget().setParent(None)
        self.container.addWidget(graph)
        plt.close(fig)

    def input_change_handler(self):
        self.error = True
        text = self.input.text()
        if text == "":
            self.text = rf'{self.symbol}(x) = '
        else:    
            self.text = self.validate_input(text)
        self.timer.start(100)

    def validate_input(self, text):
        try:
            self.expression = sympify(text)
            x = symbols('x')
            self.lambda_function = lambdify(x, self.expression, modules=['sympy'])

            expression_symbols = self.expression.free_symbols
            if len(expression_symbols) == 0 or (len(expression_symbols) == 1 and x in expression_symbols):
                self.error = False
                return rf'${self.symbol}(x) = {latex(self.expression)}$'
            
            return "Function must only contains the variable x."
            
        except Exception:
            return "Invalid syntax."

    def get_domain(self):
        if self.expression:
            x = symbols('x')
            domain = continuous_domain(self.expression, x, S.Reals)
            return domain
        else:
            return None
