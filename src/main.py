import sys
from PySide2.QtWidgets import QApplication
from gui.MainWindow import init_program

app = QApplication(sys.argv)
program = init_program()
program.window.show()

# with open("src/styles/mainStyle.qss", "r") as f:
    # _style = f.read()
    # window.setStyleSheet(_style)

program.window.showMaximized()
app.exec_()
sys.exit()
