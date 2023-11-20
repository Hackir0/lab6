from PyQt5 import QtGui, QtCore, QtWidgets
import sys
from Window import StartWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = StartWindow()
    window.show()
    print("Программа запущена")
    sys.exit(app.exec_())
