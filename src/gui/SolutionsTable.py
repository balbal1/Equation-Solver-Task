from PySide2.QtWidgets import QTableWidgetItem
from PySide2.QtCore import Qt

class SolutionsTable:
    def __init__(self, body):
        self.body = body
        self.expand()

    def show_solution(self, solutions, same_function):
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
        for index in range(self.body.rowCount(), -1, -1):
            self.body.removeRow(index)

    def set_message(self, message):
        self.body.setColumnWidth(0, 0)
        self.body.setColumnWidth(1, 348)
        self.body.insertRow(0)
        self.insert_item(message, 0, 1)

    def insert_item(self, text, row, column):
        item = QTableWidgetItem(text)
        item.setTextAlignment(Qt.AlignCenter)
        self.body.setItem(row, column, item)

    def expand(self):
        self.body.setColumnWidth(0, 100)
        self.body.setColumnWidth(1, 248)
