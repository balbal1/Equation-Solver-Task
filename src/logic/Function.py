from PySide2.QtCore import QTimer
from sympy import symbols, sympify, latex, S
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
        graph.setMaximumHeight(50)
        self.container.itemAt(0).widget().setParent(None)
        self.container.addWidget(graph)
        plt.close(fig)

    def input_change_handler(self):
        text = self.input.text()
        if text == "":
            self.text = rf'{self.symbol}(x) = '
        else:    
            try:
                self.expression = sympify(text)
                self.text = rf'${self.symbol}(x) = {latex(self.expression)}$'
            except Exception:
                self.text = "Invalid input!"

        self.timer.start(100)

    def get_domain(self):
        if self.expression:
            x = symbols('x')
            domain = continuous_domain(self.expression, x, S.Reals)
            return domain
        else:
            return None
