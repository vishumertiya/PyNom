import sys
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtWidgets import QDialogButtonBox

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        #self.setGeometry(100,100,300,200)
        #fname = QtGui.QFileDialog.getOpenFileName(self, 'Select background image', '/home/venom/lab/img/bg2.png')
        self.setStyleSheet("background-image: url(/home/venom/lab/img/bg2.png); background-repeat: no-repeat; background-position: center;")
        #self.setStyleSheet("background-image:url(/home/venom/lab/img/bg2.png);")
        self.layout  = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        #self.layout.addWidget(Frame(self))
        self.layout.addWidget(Dialog(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setMinimumSize(800,400)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        print(self.parent.width())
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel("")

        btn_size = 10

        self.btn_close = QPushButton("")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size,btn_size)
        self.btn_close.setIcon(QtGui.QIcon('img/close.png'))
        #self.btn_close.setStyleSheet("background-color: red;")

        self.btn_min = QPushButton("")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setIcon(QtGui.QIcon('img/min.png'))
        #self.btn_min.setStyleSheet("background-color: gray;")


        #self.btn_max = QPushButton("+")
        #self.btn_max.clicked.connect(self.btn_max_clicked)
        #self.btn_max.setFixedSize(btn_size, btn_size)
        #self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(0)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        #self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet("""
            background-color: black;
            color: white;
        """)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.parent.width(),
                                self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()

class Dialog(QDialog):
    #NumGridRows = 3
    #NumButtons = 4

    def __init__(self,parent):
        super(Dialog, self).__init__()
        self.createFormGroupBox()
        self.setMinimumSize(600,300)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        #self.setWindowTitle("Form Layout - pythonspot.com")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("")
        layout = QFormLayout()
        layout.addRow(QLabel("User:"), QLineEdit())
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        layout.addRow(QLabel("Password:"), e5)
        #layout.addRow(QLabel("Password:"), QComboBox())
        #layout.addRow(QLabel("Environment:"), QSpinBox())
        self.formGroupBox.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())
