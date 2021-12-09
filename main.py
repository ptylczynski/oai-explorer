import sys

from PyQt5 import QtWidgets
from qt_material import apply_stylesheet

from ui.py.main import Ui_mainWindow


class MyApp(QtWidgets.QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        # Load the login form
        self.setupUi(self)
        self.pushButton.clicked.connect(self.c)

    def c(self):
        print('sdfsd')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_amber.xml', invert_secondary=False)
    # Create class object
    form = MyApp()
    # Display the form
    form.show()
    # Start the event loop of the app or dialog box
    app.exec()
