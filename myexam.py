
import sys

from PySide6.QtWidgets import QVBoxLayout, QPushButton, QDialog, QHBoxLayout, QApplication, QGridLayout


class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        w_1 = QPushButton("Widget_1")
        w_2 = QPushButton("Widget_2")
        w_3 = QPushButton("Widget_3")
        w_4 = QPushButton("Widget_4")
        w_5 = QPushButton("Widget_5")
        w_6 = QPushButton("Widget_6")
        w_7 = QPushButton("Widget_7")
        w_8 = QPushButton("Widget_8")
        w_9 = QPushButton("Widget_9")
        w_10 = QPushButton("Widget_10")
        w_11 = QPushButton("Widget_11")

        layout_attacker = QHBoxLayout()
        layout_midfielder = QHBoxLayout()
        layout_defender = QHBoxLayout()

        layout_attacker.addWidget(w_1)
        layout_attacker.addWidget(w_2)
        layout_attacker.addWidget(w_3)

        layout_midfielder.addWidget(w_4)
        layout_midfielder.addWidget(w_5)
        layout_midfielder.addWidget(w_6)

        layout_defender.addWidget(w_7)
        layout_defender.addWidget(w_8)
        layout_defender.addWidget(w_9)
        layout_defender.addWidget(w_10)

        main_layout.addLayout(layout_attacker)
        main_layout.addLayout(layout_midfielder)
        main_layout.addLayout(layout_defender)
        main_layout.addWidget(w_11)

        # layout_3 = QVBoxLayout()
        # layout_3.addWidget(w_4)
        # layout_3.addWidget(w_5)
        #
        # layout_2 = QHBoxLayout()
        # layout_2.addWidget(w_3)
        # layout_2.addLayout(layout_3)
        #
        # layout_1 = QVBoxLayout()
        # layout_1.addWidget(w_2)
        # layout_1.addLayout(layout_2)
        #
        # main_layout.addWidget(w_1)
        # main_layout.addLayout(layout_1)

        self.setLayout(main_layout)
        self.resize(500, 500)
        self.show()

        #
        # w_1 = QPushButton("Widget_1")
        # w_2 = QPushButton("Widget_2")
        # w_3 = QPushButton("Widget_3")
        # w_4 = QPushButton("Widget_4")
        # w_5 = QPushButton("Widget_5")
        #
        #
        # layout_1 = QHBoxLayout()
        # layout_1.addWidget(w_1)
        # layout_1.addWidget(w_2)
        #
        # main_layout.addLayout(layout_1)
        # main_layout.addWidget(w_3)
        #
        # layout_2 = QHBoxLayout()
        # layout_2.addWidget(w_4)
        # layout_2.addWidget(w_5)

        # main_layout.addLayout(layout_2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main  = Main()
    main.show()
    sys.exit(app.exec())