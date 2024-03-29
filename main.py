from PyQt6 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow
import sys

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec())
