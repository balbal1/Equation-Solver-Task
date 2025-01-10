import sys
from PySide2.QtWidgets import QApplication
from gui.MainWindow import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.show()

# with open("src/styles/mainStyle.qss", "r") as f:
    # _style = f.read()
    # window.setStyleSheet(_style)

window.showMaximized()
app.exec_()
sys.exit()
