from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QMessageBox, QLineEdit, QApplication)

from mainFrame import Ui_MainWindow


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        btn.clicked.connect(self.btnOkClicked)


        id_qle = QLineEdit(self)
        id_qle.move(0, 0)

        pw_qle = QLineEdit(self)
        pw_qle.move(100, 200)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()

    def btnOkClicked(self):
        name = "park"
        # QMessageBox.information(self, "Info", name)
        ma = MainFrame()


