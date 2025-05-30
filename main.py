import sys
from PySide6 import QtWidgets


class Test(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi()
        self.setGeometry(500, 500, 500, 500)

    def setupUi(self):
        self.setLayout(QtWidgets.QGridLayout(self))
        self.dial = QtWidgets.QDial(self)
        self.layout().addWidget(self.dial)
        self.btns = [QtWidgets.QPushButton(self), QtWidgets.QPushButton(self), QtWidgets.QPushButton(self), QtWidgets.QPushButton(self)]
        for idx, btn in enumerate(self.btns):
            self.layout().addWidget(btn)
            btn.setText(str(idx))
            btn.clicked.connect(lambda x, y=idx: self.btn_clicked(y))
        # for y in range(10):
        self.dial.sliderMoved.connect(lambda x, y_=1: self.dial_change(x, y_))

    def dial_change(self, int_, counter):
        print(counter)

    def btn_clicked(self, int_):
        print(int_)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    m = Test()
    m.show()
    app.exec()