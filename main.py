import init
import val_gui as gui
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui = init.start(ui)
    MainWindow.show()
    sys.exit(app.exec_())