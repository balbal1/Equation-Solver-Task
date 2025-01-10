from PySide2.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide2.QtUiTools import QUiLoader

def MainWindow():

    def mainwindow_setup(w):
        w.setWindowTitle("MainWindow Title")

    loader = QUiLoader()
    window = loader.load("src/gui/mainwindow.ui", None)
    mainwindow_setup(window)

    return window

# class MainWindow(QMainWindow):
    
#     def __init__(self):
#         super(MainWindow, self).__init__()
