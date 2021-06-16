import sys
<<<<<<< HEAD
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):
=======
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
>>>>>>> 5b0d7849bf2e3caa6da032a871e0edb332ab6b3d

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
<<<<<<< HEAD
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
=======
        self.setWindowTitle('My First Application')
        self.move(300, 300)
        self.resize(400, 200)
>>>>>>> 5b0d7849bf2e3caa6da032a871e0edb332ab6b3d
        self.show()


if __name__ == '__main__':
<<<<<<< HEAD
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
=======
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
>>>>>>> 5b0d7849bf2e3caa6da032a871e0edb332ab6b3d
