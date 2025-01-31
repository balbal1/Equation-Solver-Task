from PySide2.QtCore import QTimer, Signal, QObject
from sympy import symbols, sympify, lambdify, latex, S, Float
from sympy.core.function import AppliedUndef
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from sympy.calculus.util import continuous_domain

class Function(QObject):
    disable = Signal(str)

    def __init__(self, symbol, input, container):
        super().__init__()
        self.text = None
        self.expression = None
        self.error = True
        self.symbol = symbol
        self.input = input
        self.container = container
        self.timer = QTimer()

        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.draw_function)

        self.input.textChanged.connect(self.input_change_handler)
        self.input_change_handler()

    def input_change_handler(self):
        """
        Handles the event of user changing function input.
        """

        self.error = True
        text = self.input.text()
        if text == "":
            self.text = rf'{self.symbol}(x) = '
        else:    
            self.text = self.validate_input(text)
        self.timer.start(100)

    def validate_input(self, text):
        """
        Check if the input function is valid and parse it.

        Args:
            text (str): The input function text.
        
        Returns:
            str: Input function latex if valid, else error message.
        """

        try:
            log_found = text.find("log10")
            while log_found != -1:
                end = text.index(")", log_found)
                text = text[:log_found+3] + text[log_found+5:end] + ",10" + text[end:]
                log_found = text.find("log10")
                
            self.expression = sympify(text)
            x = symbols('x')
            self.lambda_function = lambdify(x, self.expression, modules=['sympy'])

            expression_symbols = self.expression.free_symbols
            if len(expression_symbols) != 0 and (len(expression_symbols) != 1 or x not in expression_symbols):
                self.disable.emit("true")
                return "Function must only contains the variable x."

            if len(self.expression.atoms(AppliedUndef)) > 0:
                self.disable.emit("true")
                return f"Unknown function: {list(self.expression.atoms(AppliedUndef))[0]}"
            
            self.error = False
            self.disable.emit("false")
            return rf'${self.symbol}(x) = {latex(self.expression)}$'
            
        except Exception:
            self.disable.emit("true")
            return "Invalid syntax."

    def get_domain(self):
        """
        Gets domain of the function.
        
        Returns:
            object: Domain set object.
        """

        if self.expression:
            x = symbols('x')
            domain = continuous_domain(self.expression, x, S.Reals)
            return domain
        else:
            return None

    def evaluate_function(self, x_values, min_y, max_y):
        """
        Evaluates the function for the given inputs.

        Args:
            x_values (list): The list of x values to evaluate.
            min_y (number): The minimum value of y range to return.
            max_y (number): The maximum value of y range to return.
        
        Returns:
            list: List of corresponding y values for each x input.
        """

        y_values = []
        domain = self.get_domain()
        for value in x_values:
            if domain.contains(value):
                try:
                    y_value = Float(self.lambda_function(value)).evalf()
                except:
                    y_value = Float(self.lambda_function(value).evalf()).evalf()
                if min_y < y_value and y_value < max_y:
                    y_values.append(y_value)
                else:
                    y_values.append(float('NaN'))
            else:
                y_values.append(float('NaN'))
        return y_values

    def draw_function(self):
        """
        Updates the render of the function latex or error message.
        """
        
        fig, ax = plt.subplots()
        ax.text(0, 0.5, self.text, fontsize=20, ha='left', va='center')
        ax.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        graph = FigureCanvasQTAgg(fig)
        graph.setMaximumHeight(80)
        self.container.itemAt(0).widget().setParent(None)
        self.container.addWidget(graph)
        plt.close(fig)