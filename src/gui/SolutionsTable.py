from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt

class SolutionsTable:
    def __init__(self, body):
        self.body = body
        self.expand()

    def show_solution(self, solutions, same_function):
        """
        Updates the table data with a list of solutions.

        Args:
            solutions (list): The list of solution values to display.
            same_function (bool): Boolean that is true if the two functions are the same.
        """

        self.clear()

        if len(solutions) == 0:
            message = "The solutions are infinite" if same_function else "No solution exists"
            self.set_message(message)

        else:
            self.expand()
            for index, solution in enumerate(solutions):
                self.body.insertRow(index)
                self.insert_item("p" + str(index+1), index, 0)
                self.insert_item(str(solution), index, 1)

    def clear(self):
        """
        Clears all table rows.
        """

        for index in range(self.body.rowCount(), -1, -1):
            self.body.removeRow(index)

    def set_message(self, message):
        """
        Set a message in the table.

        Args:
            message (str): Message to display.
        """

        self.body.setColumnWidth(0, 0)
        self.body.setColumnWidth(1, 348)
        self.body.insertRow(0)
        self.insert_item(message, 0, 1)

    def insert_item(self, text, row, column):
        """
        Insert data at certain row and cloumn.

        Args:
            text (str): Data to display.
            row (int): Index of row to insert at.
            column (int): Index of column to insert at.
        """

        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.body.setItem(row, column, item)

    def expand(self):
        """
        Shows all columns of the table.
        """
        
        self.body.setColumnWidth(0, 100)
        self.body.setColumnWidth(1, 248)
