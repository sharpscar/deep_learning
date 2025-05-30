import sys, os
from PySide6.QtWidgets import *


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def __str__(self):
        return "Wow!"

    def init_ui(self):
        main_layout= QVBoxLayout()

        pushbutton = QPushButton("button 1")
        pushbutton.clicked.connect(self.button_clicked)

        main_layout.addWidget(pushbutton)

        self.lineedit = QLineEdit()
        main_layout.addWidget(self.lineedit)

        combobox = QComboBox()
        combobox.addItems(["dog","cat", "rabbit", "lion"])
        combobox.currentTextChanged.connect(self.combobox_changed) #문자열이 바뀌면 바뀐 문자열이 들어가도록 한다.
        main_layout.addWidget(combobox)

        self.lineedit_combobox = QLineEdit()
        main_layout.addWidget(self.lineedit_combobox)

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()

    def button_clicked(self):

        self.lineedit.setText("button clicked.")

    def combobox_changed(self, text_item):
        self.lineedit_combobox.setText(str(text_item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()

    print(main)
    sys.exit(app.exec())

